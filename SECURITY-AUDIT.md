# Security Audit — axios Malware Check

**Date:** 2026-04-01  
**Scope:** All public Node.js repositories owned by `webcrafter011`  
**Trigger:** Check for malicious axios versions `1.14.1` and `0.30.4`

---

## Advisory Summary

Both `axios@1.14.1` and `axios@0.30.4` are confirmed **malware** packages published to npm.  
There is **no patched version** — these packages must not be installed.

| Package | Version | Severity | Advisory |
|---------|---------|----------|----------|
| axios   | 1.14.1  | Malware  | GHSA (npm) |
| axios   | 0.30.4  | Malware  | GHSA (npm) |

---

## Repositories Checked

The following repositories were scanned for `axios` in their `package.json` files:

| Repository | File | axios Version (package.json) | Locked Version | Status |
|---|---|---|---|---|
| [Video-Transcript-Adder](https://github.com/webcrafter011/Video-Transcript-Adder) | `package.json` | `^1.7.9` | not checked | ⚠️ Range includes 1.14.1 |
| [Advanced-Todo-List-](https://github.com/webcrafter011/Advanced-Todo-List-) | `Frontend/package.json` | `^1.10.0` | not checked | ⚠️ Range includes 1.14.1 |
| [Fullstack_Open_Exercises_Solutions](https://github.com/webcrafter011/Fullstack_Open_Exercises_Solutions) | `part2/phonebook/package.json` | `^1.8.4` | not checked | ⚠️ Range includes 1.14.1 |
| [Fullstack_Open_Exercises_Solutions](https://github.com/webcrafter011/Fullstack_Open_Exercises_Solutions) | `part2/countrypedia/package.json` | `^1.8.4` | not checked | ⚠️ Range includes 1.14.1 |
| [Nexa-backend](https://github.com/webcrafter011/Nexa-backend) | `package.json` | `^1.11.0` | not checked | ⚠️ Range includes 1.14.1 |
| [full-stack-task-management-app](https://github.com/webcrafter011/full-stack-task-management-app) | `package.json` | `^1.7.9` | not checked | ⚠️ Range includes 1.14.1 |
| [Hackathon-judge-frontend](https://github.com/webcrafter011/Hackathon-judge-frontend) | `package.json` | `^1.11.0` | **1.11.0** | ✅ Safe (currently locked) |
| [Nexa-Fullstack](https://github.com/webcrafter011/Nexa-Fullstack) | `frontend/package.json` | `^1.13.2` | **1.13.2** | ✅ Safe (currently locked) |
| [Nexa-Fullstack](https://github.com/webcrafter011/Nexa-Fullstack) | `backend/package.json` | `^1.11.0` | **1.11.0** | ✅ Safe (currently locked) |

### Repositories with NO axios dependency

The following repositories were checked and do **not** use axios at all:

- [Nexa-Fullstack](https://github.com/webcrafter011/Nexa-Fullstack) (Hackathon-judge-backend)
- [craft-my-plate-backend](https://github.com/webcrafter011/craft-my-plate-backend)
- [Raygen-](https://github.com/webcrafter011/Raygen-)
- [React.js-Projects](https://github.com/webcrafter011/React.js-Projects)
- [ResourceNation-ProjectHub](https://github.com/webcrafter011/ResourceNation-ProjectHub)
- [React-Ecommerce-Website](https://github.com/webcrafter011/React-Ecommerce-Website)
- [Catch-The-Box](https://github.com/webcrafter011/Catch-The-Box)
- [ffmpeg-random-panning-effects](https://github.com/webcrafter011/ffmpeg-random-panning-effects)
- [Assembly-Endgame](https://github.com/webcrafter011/Assembly-Endgame)
- [weather-app](https://github.com/webcrafter011/weather-app)
- [Weather-Detection-App](https://github.com/webcrafter011/Weather-Detection-App)
- [Resourcenation-backend](https://github.com/webcrafter011/Resourcenation-backend)
- [banao-task-1](https://github.com/webcrafter011/banao-task-1)
- [codechef-problem-solver](https://github.com/webcrafter011/codechef-problem-solver)
- [pdf-compressor](https://github.com/webcrafter011/pdf-compressor)
- [Ecommerce-MERN-Frontend](https://github.com/webcrafter011/Ecommerce-MERN-Frontend)
- [iPhone-Website](https://github.com/webcrafter011/iPhone-Website)
- [My-resume](https://github.com/webcrafter011/My-resume)
- [Sahayak-](https://github.com/webcrafter011/Sahayak-)
- [Balaji-Super-Shoppy-](https://github.com/webcrafter011/Balaji-Super-Shoppy-)

---

## Verdict

> **No repository has `axios@1.14.1` or `axios@0.30.4` explicitly pinned.**

However, **all 9 repositories** that use axios specify a `^1.x.x` semver range. Because `^` allows any version `>= specified` and `< 2.0.0`, every one of these repos **could resolve to the malicious `1.14.1`** if:

- `package-lock.json` is deleted and `npm install` is re-run, **or**
- A fresh `npm install` is performed in a new environment

The three repos where `package-lock.json` was inspected are currently locked to safe versions (`1.11.0` or `1.13.2`), but their semver ranges still permit `1.14.1`.

---

## Recommended Actions

1. **Pin axios to a known-safe version** in all affected `package.json` files.  
   Use an exact version or a tight range that explicitly excludes `1.14.1`:
   ```json
   "axios": "1.9.0"
   ```
   *(Replace with the latest safe release from the [official axios releases](https://github.com/axios/axios/releases).)*

2. **Commit updated `package-lock.json`** after running `npm install` with the pinned version.

3. **Monitor npm advisories** for axios and other dependencies regularly.

4. **For `axios@0.30.4`** — none of the repositories use axios `0.x`, so this malicious version is **not a risk** for any of these repos.
