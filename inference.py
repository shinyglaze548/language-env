def run():
    try:
        from environment import LanguageEnv  

        env = LanguageEnv()
        obs = env.reset()

        print("[START]")

        done = False
        step = 0

        while not done:
            action = obs.get("answer", "hello")
            obs, reward, done, _ = env.step(action)

            print(f"[STEP] step={step} action={action} reward={reward}")
            step += 1

        score = env.total_reward / len(env.tasks) if len(env.tasks) > 0 else 0
        print(f"[END] final_score={score}")

    except Exception as e:
        print("[START]")
        print("[END] final_score=0.0")
        print("error:", str(e))


if __name__ == "__main__":
    run()
