import os
from openai import OpenAI
from typing import Dict, Any

cv = "ALI HUSSAIN\n" \
     "mirzaalihussain2@gmail.com | +44 7415 376512 | github.com/mirzaalihussain2\n\n" \
     "Building tech products for 5 years across B2B & B2C startups, as a Product Manager and Software Engineer.\n" \
     "Experience defining a product vision, validating customer problems, and leading an engineering squad to delivery.\n\n" \
     "EXPERIENCE\n" \
     "Gizmo AI, Software Engineer Apr 2024 — Present\n" \
     "VC-backed web & mobile app for AI-enabled learning, using LLM-generated quizzes. 117k DAU, 14x YoY revenue growth.\n\n" \
     "• Built a shareable notification with a user's weekly rank, resulting in 40% re-activation among applicable users.\n" \
     "• Developed & launched first version of in-game store, achieving above-benchmark Day 7 feature retention (72%).\n" \
     "• Reduced machine learning costs for reading PDFs by 30% by optimising the PDF import process.\n" \
     "• Improved SEO score and cut orphaned pages by 90% by redesigning public search and proliferating internal links.\n\n" \
     "Startbook, Software Engineer (1st full-time hire) Aug 2023 — Apr 2024\n" \
     "A B2B SaaS platform for founders, startups and incubators to share pitch decks, manage data, and connect with investors.\n" \
     "Clients include: Barclays, Imperial College London, LSE, UCL, KCL. Bootstrapped to 6-figure revenue.\n\n" \
     "• Eliminated 152 hours of CEO's operational work annually by refactoring backend user authentication script.\n" \
     "• Created a full-stack WYSIWYG email editor, allowing client admins to send 100s of personalised emails at once.\n" \
     "• Cut downtime by 35% through redesigning APIs to deliver smaller payloads, improve type safety & reduce errors.\n" \
     "• Scaled annual subscriptions from London universities by 125% by developing key privacy & sharing features.\n\n" \
     "Limitless Technology, Product Manager Nov 2019 — Oct 2022\n" \
     "\"Uber for customer service\": a marketplace for companies with unmet customer service demand to transact with\n" \
     "gig-workers who answer customer service tickets. 73% YoY growth. Clients incl. Microsoft, eBay, Unilever, Sony, Airbnb.\n\n" \
     "• Saved Operations team 52 hrs / month by leading an engineering team of 14 to overhaul Onboarding feature area\n" \
     "  (incl. running interviews & reviewing support tickets, designing & evangelising a roadmap, managing delivery).\n" \
     "• Managed 5-strong team to ship features reducing time to create learning material by 81% across 13 clients.\n" \
     "• Spearheaded integration with ID verification firm; verifying identities of 1000s of gig-workers across 6 markets.\n" \
     "• Shipped new set of automated emails: 63% rise in customer ratings received, 75% rise in customer resolutions.\n" \
     "• Increased gross margin by $37.7k annually on a key client by experimenting with different ticket pricing strategies.\n" \
     "• Redesigned our peer-review process to make it 5.1% faster across 129,000 customer service queries per quarter.\n" \
     "• Simulated fee-allocation algorithms in SQL & Excel: fees allocated 4.3% more equitably across 2,000 gig-workers.\n\n" \
     "Quester, Product Coach Aug 2021 — Oct 2022\n\n" \
     "• Coaching founders weekly at a pre-seed EdTech startup on Product, supported a £200k raise at a £2m valuation.\n" \
     "• Conducted 15 customer discovery interviews leading to a pivot from young professionals to school-age students.\n\n" \
     "Verisk Sequel (S&P 500), Technical Business Analyst Feb 2019 — Sep 2019\n\n" \
     "• Built modern web UIs for flagship insurance engine, used by 3000+ underwriters and brokers globally.\n" \
     "• Owned delivery of 4 features, incl. wireframes, requirements, and unblocking engineers during development.\n\n" \
     "EDUCATION\n" \
     "Oxford University, BA Philosophy, Politics & Economics Sep 2015 — Aug 2018\n\n" \
     "• JCR President (2016-17) representing 450 students, leading a team of 35 and overseeing a £28.7k annual budget.\n\n" \
     "TECHNICAL SKILLS\n\n" \
     "• Languages: TypeScript, Python, SQL, HTML, CSS.\n" \
     "• Frameworks & libraries: React (Next.js, Remix), React Native (Expo), Angular, Svelte, Express, Koa, Flask, Django.\n" \
     "• Databases: PostgreSQL, mySQL, Firebase, mongoDB, Redis.\n" \
     "• DevOps: Docker, GCP, Vercel & Heroku (for deployment), GitHub Actions (for CI), BetterStack (for observability).\n\n" \
     "INTERESTS\n\n" \
     "• Cycling: Spent 12 days bike-packing the Netherlands in Aug 2023, completed the 1000km Ronde van Nederland.\n" \
     "• Travelling: Travelled Southeast Asia Nov 2022 to Feb 2023; highlight was mountain-biking around Angkor Wat.\n" \
     "• Boxing: Competed in a white collar boxing match for CALM charity, after only 10 weeks training. Sold 36 tickets.\n" \
     "• Volunteering: Urdu translator surveying Calais 'Jungle' for Help Refugees; census published in The Guardian."

job_description = "Who we are:\n\n" \
    "We are a leader in fraud prevention and AML compliance. Our platform uses device intelligence, behavior biometrics, machine learning, and AI to stop fraud before it happens. Today, over 300 banks, retailers, and fintechs worldwide use Sardine to stop identity fraud, payment fraud, account takeovers, and social engineering scams. We have raised $145M from world-class investors, including Andreessen Horowitz, Activant, Visa, Experian, FIS, and Google Ventures.\n\n" \
    "Our culture:\n\n" \
    "We have hubs in the Bay Area, NYC, Austin, and Toronto. However, we maintain a remote-first work culture. #WorkFromAnywhere\n\n" \
    "We hire talented, self-motivated individuals with extreme ownership and high growth orientation.\n\n" \
    "We value performance and not hours worked. We believe you shouldn't have to miss your family dinner, your kid's school play, friends get-together, or doctor's appointments for the sake of adhering to an arbitrary work schedule.\n\n" \
    "Location:\n\n" \
    "UK / Germany / Bulgaria\n\n" \
    "From Home / Beach / Mountain / Cafe / Anywhere!\n\n" \
    "We are a remote-first company with a globally distributed team. You can find your productive zone and work from there.\n\n" \
    "About the role:\n\n" \
    "Sales Engineering is a team of subject matter experts who serve as the trusted technical advisor to prospective customers. You will lead prospects through the sales process by connecting their needs to Sardine's value to win new customers and drive revenue growth. You will deliver best in class product demonstrations, fill out RFPs, and win over our prospective customer's technical teams with your thought leadership and consultative approach. Internally, your insights from the field will help shape our product roadmap and will pave the way for future customers.  You will play a key role in our commitment to customer excellence and allow Sardine to stay ahead of market trends.\n\n" \
    "The SE team is a high visibility and high impact team. At the intersection of our Go-To-Market and Product and Engineering teams, we serve as the link between our customer's needs and the Sardine's capabilities, ensuring our platform is always adding value to our customer's Fraud and Compliance stack.  It's a great role for someone who enjoys learning the intricacies of a product to drive value to prospects, and leading through innovative problem-solving to convert prospects into customers. Variety, ambiguity, innovation, and ownership of complex problems are all big components of this role.\n\n" \
    "As a Sales Engineer, you will:\n\n" \
    "Support Account Executives in identifying a prospect's fraud and compliance needs.\n\n" \
    "Prepare and deliver customized demos that showcase the impact of Sardine's platform.\n\n" \
    "Interface with Security teams to articulate our security posture and successfully complete security reviews.\n\n" \
    "Complete RFPs for competitive opportunities.\n\n" \
    "Create comprehensive Solution Designs that address our prospect's needs.\n\n" \
    "Collaborate with peers to improve all processes within the Sales Engineering team.\n\n" \
    "Work together with our product and engineering teams to identify areas for improvement in our product suite and help prioritize and design solutions.\n\n" \
    "What you'll bring to Sardine:\n\n" \
    "7+ years prior experience as a Sales Engineer, System Engineer, Solutions Engineer, or similar roles\n\n" \
    "Prior experience in similar roles within the Risk, Fraud, or Compliance domain\n\n" \
    "Experience with APIs, a strong understanding of JSON, and proficiency in one or more of the following languages: Python, JavaScript, Ruby, Go, or Java. Bonus points for knowledge of web development principles and/or the ability to build internal tools using one of these languages.\n\n" \
    "Strong analytical skills: you can dig into the technical details of a problem and turn it into a proposed solution\n\n" \
    "Ability to thrive in a fast-paced remote environment working with global clients\n\n" \
    "Excellent written and verbal communication skills, including the ability to communicate complex technical and business concepts to technical and non-technical personas.\n\n" \
    "Compensation: Base pay range of $90,000 - $120,000 + Equity with tremendous upside potential + Attractive benefits"

prompt = "Compare my CV to this job description"

def send_info_to_asian():
    print("Hello sur")
    return {"message": "Hello sur"}

def send_info_to_agent():
    client = OpenAI(
        api_key=os.getenv('OPENAI_API_KEY')
    )
    
    system_prompt = """You are an expert HR professional and job matcher. 
    Analyze the provided CV against the job description and provide:
    1. Overall match score (0-100)
    2. Key strengths that align with the role
    3. Potential gaps or areas for improvement
    4. Specific recommendations
    Format your response in clear sections."""

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"CV:\n{cv}\n\nJob Description:\n{job_description}\n\nTask:\n{prompt}"}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        
        return {
            "success": True,
            "analysis": response.choices[0].message.content
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }