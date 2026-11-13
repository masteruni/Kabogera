# Builds the final mix: VO lines placed on their beats, music bed ducked under the voice, SFX on top, mastered to about -14 LUFS.
#   python3 build_audio.py   (run from audio/; needs ffmpeg, numpy)
import json, subprocess, numpy as np
SR, LEN = 48000, 25.2
def load(p, ss=None, to=None):
    cmd = ['ffmpeg', '-v', 'error'] + (['-ss', str(ss), '-to', str(to)] if ss is not None else []) + ['-i', p, '-ac', '2', '-ar', str(SR), '-f', 'f32le', '-']
    return np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, np.float32).reshape(-1, 2).astype(np.float64)
N = int(LEN * SR); vo = np.zeros((N, 2)); cfg = json.load(open('vo-lines.json'))
for ln in cfg['lines']:
    x = load(cfg['source'], ln['from'], ln['to']); f = int(0.03 * SR); x[:f] *= np.linspace(0, 1, f)[:, None]; x[-f:] *= np.linspace(1, 0, f)[:, None]
    i = int(ln['at'] * SR); n = min(len(x), N - i); vo[i:i + n] += x[:n]
# music: from 0.2s into the track so its lift (~21s in the file) meets the end card; fade in, fade out at the end
mu = load('music-sleeping-in-my-head.wav', 0.2, 0.2 + LEN); mu = np.pad(mu, ((0, max(0, N - len(mu))), (0, 0)))[:N]
t = np.arange(N) / SR; mu *= np.clip(t / 0.8, 0, 1)[:, None] * np.clip((LEN - t) / 1.8, 0, 1)[:, None]
# duck the music under the voice (smooth sidechain-style envelope)
e = np.abs(vo).max(1); w = int(0.25 * SR); e = np.convolve(e, np.ones(w) / w, 'same'); act = np.clip(e / (e.max() * 0.08), 0, 1)
k = int(0.12 * SR); act = np.convolve(act, np.ones(k) / k, 'same')
mu *= (10 ** ((-14 - 7 * act) / 20))[:, None]        # bed at -14 dB, a further -7 dB under the voice
sfx = load('sfx-mix.wav'); sfx = np.pad(sfx, ((0, max(0, N - len(sfx))), (0, 0)))[:N]
vo_ = vo * 10 ** (1.5 / 20)
mix = vo_ + mu + sfx * 0.9
np.save('/tmp/claude-0/-home-user-Kabogera/f6a396a3-cf26-58a8-b88d-b597103ea47c/scratchpad/mix.npy', mix)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f64le', '-ar', str(SR), '-ac', '2', '-i', '-', '-af', 'loudnorm=I=-14:TP=-1.0:LRA=9', '-ar', str(SR), 'Kabogera partners abroad - mix.wav'],
               input=mix.astype(np.float64).tobytes(), check=True)
for name, sig in [('vo', vo_), ('music', mu), ('sfx', sfx)]: print(name, 'peak dBFS %.1f' % (20 * np.log10(np.abs(sig).max() + 1e-9)))
