# Resume Version Control + Placement Planner System

def ats_score(resume_keywords, jd_keywords):
    matched = set(resume_keywords).intersection(set(jd_keywords))
    score = (len(matched) / len(jd_keywords)) * 100
    return score, matched

def resume_version_control():
    versions = []
    n = int(input("Enter number of resume versions: "))
    
    for i in range(n):
        data = input(f"Enter keywords for Resume Version {i+1} (comma separated): ")
        versions.append(data.split(","))

    print("\nStored Resume Versions Successfully!")
    return versions

def placement_planner():
    applications = []
    m = int(input("\nEnter number of job applications: "))
    
    for i in range(m):
        company = input("Enter company name: ")
        role = input("Enter role: ")
        status = input("Enter status (Applied/Interview/Selected): ")
        
        applications.append({
            "company": company,
            "role": role,
            "status": status
        })

    print("\nJob Applications Tracked Successfully!")
    return applications

def main():
    print("=== AI Resume VC + Placement Planner ===")

    # Resume Versions
    versions = [
        ["python", "ml", "sql"],
        ["java", "dsa", "dbms"]
    ]

    jd_keywords = ["python", "sql", "ai"]

    print("\n--- ATS SCORE ANALYSIS ---")
    for i, resume in enumerate(versions):
        score, matched = ats_score(resume, jd_keywords)
        print(f"\nResume Version {i+1}:")
        print("ATS Score:", round(score, 2), "%")
        print("Matched Keywords:", matched)

    applications = [
        {"company": "TCS", "role": "Developer", "status": "Applied"},
        {"company": "Infosys", "role": "Analyst", "status": "Interview"}
    ]

    print("\n--- APPLICATION SUMMARY ---")
    for app in applications:
        print(f"{app['company']} - {app['role']} -> {app['status']}")

    print("\nPipeline executed successfully!")

if __name__ == "__main__":
    main()