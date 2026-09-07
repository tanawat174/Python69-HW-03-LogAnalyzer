def analyze_user_activity(log_file_path: str) -> dict:
    #your code here
    total_users = []
    action_counts = {}
    user_sessions = {}

    with open(log_file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            if len(parts) < 4:
                continue  
                
            timestamp = parts[0]
            user_id = parts[1]
            action = parts[2]
            try:
                duration = float(parts[3])
            except ValueError:
                duration = 0.0

            total_users.append(user_id)
            action_counts[action] = action_counts.get(action, 0) + 1
            user_sessions[user_id] = user_sessions.get(user_id, 0.0) + duration

    if user_sessions:
        most_active_user = max(user_sessions, key=user_sessions.get)
        total_duration = sum(user_sessions.values())
        total_sessions = sum(action_counts.values())
        average_session_time = total_duration / total_sessions if total_sessions > 0 else 0.0
    else:
        most_active_user = None
        average_session_time = 0.0

    result = {
        "total_users": len(total_users),
        "action_counts": action_counts,
        "most_active_user": most_active_user,
        "average_session_time": round(average_session_time, 1)
    }
    
    return result

if __name__ == "__main__":
    result = analyze_user_activity("activity.log")
    from pprint import pprint
    pprint(result)

# {'action_counts': {'login': 2, 'logout': 2, 'submit': 1, 'view': 2},
#  'average_session_time': 160.0,
#  'most_active_user': 'u002',
#  'total_users': 2}
