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

# navigation menu items
nav_items = [
    {"name": "Home", "url": "/"},
    {"name": "Work Experience", "url": "/work-experience"},
    # future items will be added here:
    # {"name": "Education", "url": "/education"},
    # {"name": "Hobbies", "url": "/hobbies"},
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
