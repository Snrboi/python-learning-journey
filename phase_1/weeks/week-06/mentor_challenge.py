developer_skills = ["Python", "Git", "SQL", "Python", "APIs"]
ai_skills = ["Python", "Machine Learning", "APIs", "Python"]

developer = set(developer_skills)
ai = set(ai_skills)

both_skills = developer | ai
joint_skills = developer & ai
dev_skill = developer - ai
ai_skill = ai - developer