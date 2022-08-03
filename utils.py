import json


def load_candidates():
    """загрузит данные из файла и показывает всех кандидатов"""
    with open("candidates.json", 'r', encoding="utf-8") as f:
        candidates = json.load(f)

    result = ""
    for candidate in candidates:
        result += f"""\n{candidate['name']} 
{candidate['position']} 
{candidate['skills']}\n """
    return result

def get_by_pk(pk):
    """вернет кандидата по pk"""
    with open("candidates.json", 'r', encoding="utf-8") as f:
        candidates = json.load(f)

    result = ""
    for candidate in candidates:
        if candidate['pk'] == pk:
            result += f"""\n{candidate['name']} 
{candidate['position']} 
{candidate['skills']}\n """

    return result


def get_by_skill(skill_name):
    """вернет кандидатов по навыку"""
    with open("candidates.json", 'r', encoding="utf-8") as f:
        candidates = json.load(f)

    result = ""
    for candidate in candidates:
        skills = candidate['skills'].lower()
        skills = skills.split(", ")

        for skill in skills:
            if skill_name == skill:
                result += f"""\n{candidate['name']} 
{candidate['position']} 
{candidate['skills']}\n """
    return result


print(get_by_skill('python'))