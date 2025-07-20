from agents import function_tool

@function_tool
def get_career_roadmap(field: str) -> str:
    maps = {
        "software engineer": "Learn Python,DSA, web dev, and build projects.",
        "data science": "Learn Python, stats, ML, and data tools to analyze data and build smart models.",
        "graphic designer": "Learn design basics, tools like Photoshop/Figma, and build a creative portfolio.",
        "ai": "Learn Python, math (linear algebra, stats), machine learning, and build AI projects."
    }
    return maps.get(field.lower(), "No roadmap found for that field.")
