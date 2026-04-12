import sys

def run():
    print("[START]")  # print immediately

    try:
        from environment import LanguageEnv

        env = LanguageEnv()
        obs = env.reset()

        done = False
        step = 0

        while not done:
            try:
                action = obs.get("answer", "hello")
                obs, reward, done, _ = env.step(action)
                print(f"[STEP] step={step} action={action} reward={reward}")
                step += 1
            except Exception as step_error:
                print(f"[STEP] step={step} action=error reward=0.0")
                break

        try:
            score = env.total_reward / len(env.tasks) if len(env.tasks) > 0 else 0
        except:
            score = 0.0

        print(f"[END] final_score={score}")

    except Exception as e:
        print(f"[END] final_score=0.0")
        print("error:", str(e))


if __name__ == "__main__":
    try:
        run()
    except Exception as fatal:
        print("[START]")
        print("[END] final_score=0.0")
        print("fatal:", str(fatal))
        sys.exit(0)
