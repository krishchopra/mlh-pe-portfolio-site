import os
from flask import Flask, request
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape
from peewee import *
from playhouse.shortcuts import model_to_dict
import datetime

load_dotenv()
app = Flask(__name__)

# connect to database
mydb = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306,
)

print(mydb)


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb


mydb.connect()
mydb.create_tables([TimelinePost])

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

# travel/map data
travel_data = {
    "visited_places": [
        # Canada
        {
            "name": "Toronto",
            "country": "Canada",
            "lat": 43.6532,
            "lng": -79.3832,
            "flag": "🇨🇦",
            "description": "Canada's largest city and financial center",
        },
        {
            "name": "Vaughan",
            "country": "Canada",
            "lat": 43.8361,
            "lng": -79.4985,
            "flag": "🇨🇦",
            "description": "Suburban city north of Toronto",
        },
        {
            "name": "Niagara Falls",
            "country": "Canada",
            "lat": 43.0896,
            "lng": -79.0849,
            "flag": "🇨🇦",
            "description": "Famous waterfall on US-Canada border",
        },
        {
            "name": "Waterloo",
            "country": "Canada",
            "lat": 43.4643,
            "lng": -80.5204,
            "flag": "🇨🇦",
            "description": "University town, home to University of Waterloo",
        },
        # United States
        {
            "name": "Denver",
            "country": "United States",
            "lat": 39.7392,
            "lng": -104.9903,
            "flag": "🇺🇸",
            "description": "Mile High City, Colorado's capital",
        },
        {
            "name": "Salt Lake City",
            "country": "United States",
            "lat": 40.7608,
            "lng": -111.8910,
            "flag": "🇺🇸",
            "description": "Utah's capital, near the Great Salt Lake",
        },
        {
            "name": "Las Vegas",
            "country": "United States",
            "lat": 36.1699,
            "lng": -115.1398,
            "flag": "🇺🇸",
            "description": "Entertainment capital of the world",
        },
        {
            "name": "Chicago",
            "country": "United States",
            "lat": 41.8781,
            "lng": -87.6298,
            "flag": "🇺🇸",
            "description": "Windy City, Illinois' largest city",
        },
        {
            "name": "New York City",
            "country": "United States",
            "lat": 40.7128,
            "lng": -74.0060,
            "flag": "🇺🇸",
            "description": "The Big Apple, most populous US city",
        },
        {
            "name": "St. Louis",
            "country": "United States",
            "lat": 38.6270,
            "lng": -90.1994,
            "flag": "🇺🇸",
            "description": "Gateway to the West, Missouri",
        },
        {
            "name": "San Francisco",
            "country": "United States",
            "lat": 37.7749,
            "lng": -122.4194,
            "flag": "🇺🇸",
            "description": "Golden Gate City, California",
        },
        {
            "name": "Los Angeles",
            "country": "United States",
            "lat": 34.0522,
            "lng": -118.2437,
            "flag": "🇺🇸",
            "description": "City of Angels, California",
        },
        # Cuba
        {
            "name": "Varadero",
            "country": "Cuba",
            "lat": 23.1540,
            "lng": -81.2520,
            "flag": "🇨🇺",
            "description": "Beautiful beach resort town",
        },
        # India
        {
            "name": "New Delhi",
            "country": "India",
            "lat": 28.6139,
            "lng": 77.2090,
            "flag": "🇮🇳",
            "description": "Capital of India",
        },
        {
            "name": "Chandigarh",
            "country": "India",
            "lat": 30.7333,
            "lng": 76.7794,
            "flag": "🇮🇳",
            "description": "Planned city, capital of Punjab and Haryana",
        },
        {
            "name": "Agra",
            "country": "India",
            "lat": 27.1767,
            "lng": 78.0081,
            "flag": "🇮🇳",
            "description": "Home to the iconic Taj Mahal",
        },
        # Mexico
        {
            "name": "Cancun",
            "country": "Mexico",
            "lat": 21.1619,
            "lng": -86.8515,
            "flag": "🇲🇽",
            "description": "Popular beach destination on Caribbean coast",
        },
        # Switzerland
        {
            "name": "Interlaken",
            "country": "Switzerland",
            "lat": 46.6863,
            "lng": 7.8632,
            "flag": "🇨🇭",
            "description": "Alpine resort town between two lakes",
        },
        {
            "name": "Geneva",
            "country": "Switzerland",
            "lat": 46.2044,
            "lng": 6.1432,
            "flag": "🇨🇭",
            "description": "International city, home to UN offices",
        },
        # France
        {
            "name": "Paris",
            "country": "France",
            "lat": 48.8566,
            "lng": 2.3522,
            "flag": "🇫🇷",
            "description": "City of Light, capital of France",
        },
        {
            "name": "Versailles",
            "country": "France",
            "lat": 48.8014,
            "lng": 2.1301,
            "flag": "🇫🇷",
            "description": "Historic royal residence near Paris",
        },
        # Czech Republic
        {
            "name": "Prague",
            "country": "Czech Republic",
            "lat": 50.0755,
            "lng": 14.4378,
            "flag": "🇨🇿",
            "description": "Golden City, capital of Czech Republic",
        },
        # Germany
        {
            "name": "Frankfurt",
            "country": "Germany",
            "lat": 50.1109,
            "lng": 8.6821,
            "flag": "🇩🇪",
            "description": "Financial center of Germany",
        },
    ],
    "countries_visited": [
        {"name": "Canada", "flag": "🇨🇦", "cities_count": 4},
        {"name": "United States", "flag": "🇺🇸", "cities_count": 8},
        {"name": "Cuba", "flag": "🇨🇺", "cities_count": 1},
        {"name": "India", "flag": "🇮🇳", "cities_count": 3},
        {"name": "Mexico", "flag": "🇲🇽", "cities_count": 1},
        {"name": "Switzerland", "flag": "🇨🇭", "cities_count": 2},
        {"name": "France", "flag": "🇫🇷", "cities_count": 2},
        {"name": "Czech Republic", "flag": "🇨🇿", "cities_count": 1},
        {"name": "Germany", "flag": "🇩🇪", "cities_count": 1},
    ],
}

nav_items = [
    {"name": "Home", "url": "/"},
    {"name": "Work Experience", "url": "/work-experience"},
    {"name": "Education", "url": "/education"},
    {"name": "Hobbies", "url": "/hobbies"},
    {"name": "Map", "url": "/map"},
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


@app.route("/map")
def map_page():
    # use jinja to render template
    html_content = render_jinja_template(
        "map.html",
        title="Travel Map - Krish Chopra",
        travel_data=travel_data,
        nav_items=nav_items,
        current_page="Map",
    )
    return html_content


@app.route("/api/timeline_post", methods=["POST"])
def post_time_line_post():
    name = request.form["name"]
    email = request.form["email"]
    content = request.form["content"]
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)


@app.route("/api/timeline_post", methods=["GET"])
def get_time_line_post():
    return {
        "timeline_posts": [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }


@app.route("/api/timeline_post/<int:post_id>", methods=["DELETE"])
def delete_timeline_post(post_id):
    try:
        post = TimelinePost.get(TimelinePost.id == post_id)
        post.delete_instance()
        return {"message": f"Timeline post {post_id} deleted successfully"}, 200
    except TimelinePost.DoesNotExist:
        return {"error": f"Timeline post {post_id} not found"}, 404
    except Exception as e:
        return {"error": f"Failed to delete timeline post: {str(e)}"}, 500
