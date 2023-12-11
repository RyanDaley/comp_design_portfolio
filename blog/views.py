from django.shortcuts import render
from datetime import date

posts = [
    {
        "slug": "coral-house",
        "image": "houseRendering.png",
        "author": "Ryan Daley",
        "date": date(2020, 7, 21),
        "title": "Coral House",
        "excerpt": "An exploration into coral growth algorithms and their applications in architectural design.",
        "content": """The Coral House is an exploration into differential growth algorithms for architecture.
                      The growth logic is inspired by the biological growth principals of coral pollips. 
                      Our team of computational designers partnered with Biology students from the University 
                      of Tubingen to realize this interdisciplanary biomimetic design. This project involved 
                      investigating a biological specimen and isolating its key structural principals, then 
                      abstracting these principals into computational and architectural design."""
    },
    {
        "slug": "chalice-pavilion",
        "image": "04.jpg",
        "author": "Ryan Daley",
        "date": date(2020, 7, 21),
        "title": "Chalice Pavilion",
        "excerpt": "a 2-Story concrete structure that is supported by columns designed as shells",
        "content": """The goal was to design a 2-Story concrete structure that is supported by columns designed as shells, 
        and to opimize the structural design through Finite Element Analysis, Dynamic Relaxation, and an Evolutionary Solver. 
        This structure was imagined to be realized in a similar manner to the Stuttgart 21 Train Station designed by Frei Otto.
        
        After a form finding exploration process, chalice shaped columns were ultimately settled upon. These are effective at 
        reducing punching shear on the roof slab, but they also redistribute lateral loads effectively through their funicular shape. 
        With this general morphology, it became a matter of decerning the optimal shape, angle, placement, and cross section.
        
        To optimize the structure, this project employs a feeback loop between three programs: Kangaroo for Dynamic Relaxation, 
        Karawmba for Finite Element Analysis, and Galapagos for Evolutionary Solver. This feedback loop required several iterations 
        to determine all the final metrics. This is because not all of the boundary conditions were determined by the designer, and 
        were instead allowed to be emergent."""
    },
    {
        "slug": "timber-building-system",
        "image": "render_LCRL.jpg",
        "author": "Ryan Daley",
        "date": date(2022, 10, 15),
        "title": "Coral House",
        "excerpt": "design and fabricate a novel timber building system",
        "content": """Collectively, the entire ITECH class of 2021 worked together to design and fabricate a novel timber building 
        system. The construction industry is trending towards more timber usage; it is an environmentally sustainable material that 
        is renewable and sequesters carbon from the atmosphere. Further, heavy timber is a fire safe material. However, timber is 
        typically employed in very rigid grids that span in one principal direction. This makes for a limited architectural expression 
        that is not as freeform as other materialities such as concrete. The aim of this collaborative effort was to employ timber in a 
        way that allows for more design freedom, particularly in the column layout. The proposed system is a type of layered floor panel
        with CLT plates on the outsides sandwiching timber webs within. Through computational design and digital fabrication, the system 
        can have a local response to the dynamic conditions, and achieve all the metrics of success."""
    },

]

# Create your views here.
def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html")

def post_details(request, slug):
    return render(request, "blog/post-detail.html")