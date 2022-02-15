import json
from pprint import pprint as pp


def load_candidates():
    """Загрузка всех данных их файла"""
    with open("candidates.json", "r", encoding="utf8") as read_file:
        candidates = json.load(read_file)

    return candidates


def get_candidate_all():
    """Выводит всех кандидатов"""
    return load_candidates()


def get_candidates_by_skill(skill):
    """Выводит кандидатов по скилам"""
    candidates = load_candidates()
    skilled_candidates = []
    skill_lower = skill.lower()

    for candidate in candidates:
        candidate_skills = candidate["skills"].lower().split(", ")
        if skill_lower in candidate_skills:
            skilled_candidates.append(candidate)

    return skilled_candidates


def get_candidate_by_id(uid):
    """Выводит кандидата по id"""
    candidates = load_candidates()
    for candidate in candidates:
        if candidate["id"] == uid:
            return candidate

def build_preformatted_list(candidates):
    """Функция принимает в себя список кандидатов, и красиво форматирует их
    в список"""
    page_content = ""

    for candidate in candidates:
        page_content += candidate["name"] + "\n"
        page_content += candidate["position"] + "\n"
        page_content += candidate["skills"] + "\n"
        page_content += "\n"

    return "<pre>" + page_content + "<pre>"