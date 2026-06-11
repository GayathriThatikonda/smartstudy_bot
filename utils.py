def safe_execute(func, *args, fallback="Something went wrong. Please try again.", **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print(f"[ERROR]: {e}")
        return fallback