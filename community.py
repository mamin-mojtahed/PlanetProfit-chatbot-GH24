import streamlit as st

st.title("Explore Community Programs")

programs = [
    {
        "title": "LoveMyHood Matching Grant | City of Kitchener",
        "description": "Supports resident-led neighbourhood-level projects (City of Kitchener)",
        "link": "https://www.lovemyhood.ca/en/tools-money/neighbourhood-matching-grant.aspx",
        "image_link": "https://www.lovemyhood.ca/en/rotatingimages/navTab02/CSD-NDO-LB-CrosswalkSocks-min.jpg"
    },
    {
        "title": "Community Development Infrastructure Program | City of Kitchener",
        "description": "Offers grants of up to $10,000 for community development projects",
        "link": "https://www.kitchener.ca/en/taxes-utilities-and-finance/community-development-infrastructure-program.aspx",
        "image_link": "https://www.kitchener.ca/en/resourcesGeneral/Images/Homepage-images/Spring_Banner1_Art.png"
    },
    {
        "title": "Depave Paradise Project | REEP Green Solutions",
        "description": "An initiative to help guide transforming paved areas into green space",
        "link": "https://reepgreen.ca/depave",
        "image_link": "https://reepgreen.ca/wp-content/uploads/2020/09/DSC_0336-scaled.jpg"
    },
    {
        "title": "Ontario Electricity Support Program",
        "description": "Provides low-income households with support on electricity bills",
        "link": "https://ontarioelectricitysupport.ca",
        "image_link": "https://ontarioelectricitysupport.ca/images/OESP_Webpage_Graphic.jpg"
    },
    {
        "title": "Community Environmental Fund | Region of Waterloo",
        "description": "Provides financial support to environmental stewardship projects",
        "link": "https://natural-resources.canada.ca/energy-efficiency/homes/canada-greener-homes-initiative/canada-greener-homes-loan/24286",
        "image_link": "https://natural-resources.canada.ca/sites/nrcan/files/science-and-data/funding-and-partnerships/greener-homes/20210728-002_Canada%20Greener%20Homes%20Loan_webBanners_ENG.jpg"
    },
    {
        "title": "See All [PDF]",
        "description": "Explore more community programs and grants available in your community",
        "link": "https://github.com/mamin-mojtahed/PlanetProfit-chatbot-GH24/raw/master/Climate_Sustainability_Programs.pdf",
        "image_link": "https://cdn-icons-png.flaticon.com/512/3212/3212250.png"
    }
]


# Create a 2x3 grid to display the programs
cols = st.columns(3)

for i, program in enumerate(programs):
    col = cols[i % 3]
    with col:
        st.markdown(f"""
        <div style="display: flex; flex-direction: column; align-items: center; height: 550px;">
            <img src="{program['image_link']}" alt="{program['title']}" style="width:100%; height:200px; object-fit: cover;">
            <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between; text-align: center;">
            <div>
            <h3>{program['title']}</h3>
            <p>{program['description']}</p>
            </div>
            <div style="height: 100px;">
            <a href="{program['link']}">Learn more ></a>
            </div>
            </div>
        </div>
        <style>
            @media (max-width: 640px) {{
            div[style*="height: 550px;"] {{
                height: 400px !important;
            }}
            }}
        </style>
        """, unsafe_allow_html=True)
