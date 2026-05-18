from pyscript import document

photos = [

    {
        "img":"sabayang.png",
        "title":"Sabayang Pagbigkas",
        "desc":"JCO"
    },

    {
        "img":"last.png",
        "title":"Last Day",
        "desc":"Last time together"
    },

    {
        "img":"foodfair.png",
        "title":"Food Fair",
        "desc":"Minimart"
    },

    {
        "img":"intrams.png",
        "title":"Intramurals",
        "desc":"Sports activities"
    },

    {
        "img":"christmas.png",
        "title":"Christmas Party",
        "desc":"Celebrating"
    },

    {
        "img":"outside.jpg",
        "title":"Class Bonding",
        "desc":"Out of school activities"
    }

]

gallery = document.getElementById("gallery")

for p in photos:

    gallery.innerHTML += f"""

    <div class="col-md-4 mb-4">

        <div class="card shadow">

            <img src="{p['img']}"
            class="card-img-top">

            <div class="card-body">

                <h5>{p['title']}</h5>

                <p>{p['desc']}</p>

            </div>

        </div>

    </div>

    """