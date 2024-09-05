# refactor.py
import json


def refactor_match_data(match):
    try:
        name_parts = match['name'].split('\n')
        time = name_parts[0].strip()
        match_type = name_parts[1].strip()
        team1 = name_parts[2].strip()
        team2 = name_parts[3].strip()

        score_parts = name_parts[4:6]
        score = f"{score_parts[0].strip()} - {score_parts[1].strip()}"

        current_score_parts = match['current_score'].split('\n')
        win_odds = {
            "1": current_score_parts[0].strip(),
            "x": current_score_parts[1].strip(),
            "2": current_score_parts[2].strip()
        }

        next_goal_parts = current_score_parts[3:6]
        next_goal_odds = {
            "1": next_goal_parts[0].strip(),
            "x": next_goal_parts[1].strip(),
            "2": next_goal_parts[2].strip()
        }

        refactored_match = {
            "id": match['id'],
            "time": time,
            "match_type": match_type,
            "team1": team1,
            "team2": team2,
            "score": score,
            "win_odds": win_odds,
            "next_goal_odds": next_goal_odds
        }

        return refactored_match

    except Exception as e:
        print(f"Error refactoring match {match['id']}: {e}")
        return None


def refactor_all_matches(match_data):
    return [refactor_match_data(match) for match in match_data if refactor_match_data(match) is not None]
