import os
from flask import Flask, request
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape

load_dotenv()
app = Flask(__name__)

# create Jinja2 Environment
jinja_env = Environment(
    loader=FileSystemLoader("app/templates"),
    autoescape=select_autoescape(["html", "xml"]),
)

# work experience data
work_experiences = [
    {
        "company": "BirdseyePost",
        "position": "Software Engineer Intern",
        "location": "Toronto, ON",
        "duration": "Jan. 2025 - Apr. 2025",
        "logo_placeholder": "birdseyepost-logo.png",
        "company_url": "https://birdseyepost.com/",
        "achievements": [
            "Spearheaded full-stack development and unit/E2E testing of SnapCapture (<strong>FastAPI</strong>, <strong>React</strong>, <strong>Redis</strong>, <strong>GCP Pub/Sub</strong>, <strong>Terraform</strong>, <strong>Pytest</strong>, <strong>Playwright</strong>)—a new real-time engagement & attribution system that increased average app session duration by 35%",
            "Built internal web portal for managing print orders using <strong>Next.js</strong> & <strong>Postgres</strong>, enhancing visibility and managing over $400K in ARR",
            "Made business analytics dashboard (<strong>Databricks</strong>, <strong>SQL</strong>) to process 4M+ profiles—boosted sales call conversion from 6% to 18%",
            "Created cart abandonment data ingestion pipeline with the <strong>Shopify API</strong>, deploying via <strong>Docker</strong> & <strong>Kubernetes</strong> to double throughput",
        ],
    },
    {
        "company": "Encore (YC F24)",
        "position": "Software Engineer Contractor",
        "location": "San Francisco, CA",
        "duration": "Oct. 2024 - Present",
        "logo_placeholder": "encore-logo.png",
        "company_url": "https://www.trycandle.app/",
        "achievements": [
            "Led in-app messaging & sharing feature for iOS/Android app (<strong>React Native</strong>, <strong>Swift</strong>)—3,000+ chat threads now being created daily",
            "Shipped AI feature for couples to discover personalized, local date ideas (<strong>GPT 4.1 API</strong>)—grew premium user conversion by 8%",
            "Optimized <strong>React hooks</strong> & function calls to reduce database bandwidth costs by 22%, supporting 10,000+ daily active users",
        ],
    },
    {
        "company": "Garage (YC W24)",
        "position": "Software Engineer Intern",
        "location": "New York City, NY",
        "duration": "May 2024 - Aug. 2024",
        "logo_placeholder": "garage-logo.png",
        "company_url": "https://www.withgarage.com/",
        "achievements": [
            "Built website features and improved search/sorting algorithms with <strong>Next.js</strong> & <strong>Express</strong>, growing site traffic by 65% to 1,000+ DAUs",
            "Architected truck recommendation system using embeddings (<strong>OpenAI API</strong>, <strong>Pinecone</strong>) and AI appraisal tool (92% accuracy)",
            "Assembled web scraping pipeline (<strong>Python</strong>, <strong>Beautiful Soup</strong>) to aggregate dataset of 1,500+ fire trucks and inform pricing",
        ],
    },
    {
        "company": "Royal Bank of Canada",
        "position": "Software Developer Intern",
        "location": "Toronto, ON",
        "duration": "Jul. - Aug. 2023 & Jul. - Aug. 2022",
        "logo_placeholder": "rbc-logo.png",
        "company_url": "https://www.rbc.com/about-rbc.html",
        "achievements": [
            "Automated PDF data extraction process with character recognition (<strong>Java</strong>, <strong>Tesseract OCR</strong>) to cut manual data entry time by 75%",
            "Processed <strong>RESTful API</strong> requests and improved system architecture to be able to handle 300,000 legal compliance cases per year",
            "Worked in weekly agile sprints to develop a secure internal URL shortener (<strong>Node.js</strong>, <strong>React</strong>, <strong>PostgreSQL</strong>), saving 50+ hours/month",
        ],
    },
    {
        "company": "Hatch Coding",
        "position": "Software Developer Intern",
        "location": "Toronto, ON",
        "duration": "Jul. 2021 - Sep. 2021",
        "logo_placeholder": "hatch-logo.png",
        "company_url": "https://x.com/hatchcoding",
        "achievements": [
            "Contributed to and refactored core <strong>Python</strong>/<strong>JavaScript</strong> code across 400+ student projects, enhancing maintainability",
            "Improved usability and visual appeal of project templates using <strong>p5.js</strong> and <strong>Processing.py</strong>, boosting learner engagement by 19%",
        ],
    },
]

# Hobbies data
hobbies = [
    {
        "hobby": "Music",
        "activity": "Singing & Playing Guitar",
        "duration": "8+ years",
        "image_placeholder": "music-hobby.png",
        "description": "Been singing and playing the guitar for the past 8 years! Music is my creative outlet and helps me unwind after long coding sessions.",
        "details": [
            "Performed at various local venues and open mic nights",
            "Self-taught guitarist with focus on acoustic techniques",
            "Enjoy covering songs across multiple genres from pop to hip-hop",
            "Music theory knowledge helps with both composition and improvisation",
        ],
    },
    {
        "hobby": "Sports",
        "activity": "Badminton",
        "duration": "5+ years",
        "image_placeholder": "badminton-hobby.png",
        "description": "My favourite form of cardio! There's nothing quite like the fast-paced, strategic gameplay of badminton.",
        "details": [
            "Regular player at local clubs and recreational leagues",
            "Excellent cardiovascular workout that keeps me in shape",
            "Developed quick reflexes and strategic thinking skills",
            "Love the combination of power, precision, and endurance required",
        ],
    },
    {
        "hobby": "Magic",
        "activity": "Magic Tricks",
        "duration": "3+ years",
        "image_placeholder": "magic-hobby.png",
        "description": "Practicing magic tricks with David Blaine as my idol. The art of illusion fascinates me and parallels problem-solving in programming.",
        "details": [
            "Specialize in close-up magic and card tricks",
            "Performed for friends, family, and small gatherings",
            "Study the psychology behind misdirection and audience engagement",
            "Appreciate the precision and practice required to master each trick",
        ],
    },
    {
        "hobby": "Winter Sports",
        "activity": "Skiing",
        "duration": "6+ years",
        "image_placeholder": "skiing-hobby.png",
        "description": "Blue Mountain is my favorite ski resort! Nothing beats the thrill of carving down fresh powder on a crisp winter day.",
        "details": [
            "Intermediate to advanced level skier with experience on various terrains",
            "Blue Mountain in Ontario is my go-to destination for weekend trips",
            "Enjoy both groomed runs and off-piste adventures",
            "Winter sports help me stay active during the colder months",
        ],
    },
    {
        "hobby": "Puzzles",
        "activity": "Speedsolving Rubik's Cube",
        "duration": "4+ years",
        "image_placeholder": "rubiks-hobby.png",
        "description": "Can solve the Rubik's cube in under 20 seconds! The logical patterns and algorithms appeal to my programming mindset.",
        "details": [
            "Personal best time of 17.26 seconds using CFOP method",
            "Memorized over 50 different algorithms for various cube states",
            "Enjoy the mathematical precision and pattern recognition involved",
            "Regularly practice to maintain speed and explore new solving methods",
        ],
    },
]

# Education data
education = [
    {
        "institution": "University of Waterloo",
        "degree": "Bachelor of Computer Science (BCS)",
        "specialization": "Artificial Intelligence & Business Specialization",
        "duration": "2023 - 2027",
        "logo_placeholder": "waterloo-logo.png",
        "institution_url": "https://uwaterloo.ca/",
        "grade": "GPA: 3.7/4.0",
        "status": "Current",
        "activities": [
            "Data Science Club",
            "Wat Street",
            "Waterloo Blockchain",
            "WATonomous",
            "Math Faculty Orientation Leader",
            "Computer Science Club",
            "Tech+ UW",
            "Badminton Club",
            "Intramural Volleyball",
        ],
        "achievements": [
            "Faculty of Mathematics National Scholarship ($25,000)",
            "University of Waterloo Alumni Scholarship ($8,000)",
            "University of Waterloo President's Scholarship of Distinction ($2,000)",
        ],
    },
    {
        "institution": "International Baccalaureate",
        "degree": "IB Diploma",
        "specialization": "",
        "duration": "2021 - 2023",
        "logo_placeholder": "ib-logo.png",
        "institution_url": "https://www.ibo.org/",
        "status": "Completed",
        "grade": "IB Score: 40/45 points",
        "subjects": {
            "Higher Level (HL)": ["English A Literature", "Economics", "Chemistry"],
            "Standard Level (SL)": ["Mathematics A&A", "Physics", "French B"],
            "Other Credits": ["Theory of Knowledge (Philosophy)"],
        },
        "activities": [],
        "achievements": [],
    },
    {
        "institution": "Bayview Secondary School",
        "degree": "Ontario Secondary School Diploma (OSSD)",
        "specialization": "",
        "duration": "2019 - 2023",
        "logo_placeholder": "bayview-logo.jpeg",
        "institution_url": "http://www.yrdsb.ca/schools/bayview.ss/Pages/default.aspx",
        "status": "Completed",
        "grade": "Grade 12 Top 6 Course Average: 99.2%",
        "activities": [
            "Bayview Entrepreneurs (President)",
            "DECA (Trainer, Junior Representative, and Competitor)",
            "Wharton Global Investment Competition (Team Member)",
            "FBLA (Lead Marketing Trainer and Competitor)",
            "Debate Club (Junior Executive)",
            "Public Speaking Club",
            "Mathematics Club",
            "Badminton Team",
            "Tennis Team",
        ],
        "achievements": [
            "Recipient of IB Economics Subject Award",
            "Academic Honour Roll achieved for all enrolled semesters of school (Grade 9-12)",
            "Ontario Scholar Award recipient",
        ],
    },
]

# navigation menu items
nav_items = [
    {"name": "Home", "url": "/"},
    {"name": "Work Experience", "url": "/work-experience"},
    {"name": "Education", "url": "/education"},
    {"name": "Hobbies", "url": "/hobbies"},
    # future items will be added here
    # {"name": "Countries Visited", "url": "/countries"},
]


def render_jinja_template(template_name, **context):
    """
    Use Jinja to load and render templates.
    """
    # load template using Jinja2 Environment
    template = jinja_env.get_template(template_name)
    return template.render(**context)


@app.route("/")
def index():
    # use Jinja to render template
    html_content = render_jinja_template(
        "index.html",
        title="Krish Chopra",
        url=os.getenv("URL"),
        nav_items=nav_items,
        current_page="Home",
    )
    return html_content


@app.route("/work-experience")
def work_experience():
    # use Jinja to render template
    html_content = render_jinja_template(
        "work_experience.html",
        title="Work Experience - Krish Chopra",
        work_experiences=work_experiences,
        nav_items=nav_items,
        current_page="Work Experience",
    )
    return html_content


@app.route("/hobbies")
def hobbies_page():
    # use jinja to render template
    html_content = render_jinja_template(
        "hobbies.html",
        title="Hobbies - Krish Chopra",
        hobbies=hobbies,
        nav_items=nav_items,
        current_page="Hobbies",
    )
    return html_content


@app.route("/education")
def education_page():
    # use jinja to render template
    html_content = render_jinja_template(
        "education.html",
        title="Education - Krish Chopra",
        education=education,
        nav_items=nav_items,
        current_page="Education",
    )
    return html_content
