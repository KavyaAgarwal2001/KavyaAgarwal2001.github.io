import os

PHOTO_ROOT = "images/photos"
OUTPUT_FILE = "photos.html"
IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png", ".gif", ".webp"]

# Define your trips here
TRIPS = [
    {
        "folder": "shimla",
        "title": "Shimla, 2024",
        "description": (
            "These photos are from my trip to Shimla in 2024 with a friend — my second time carrying a camera on a trip. "
            "(The first was a day trip to New York, which may or may not count as a real <em>trip</em>, but let’s not split hairs.)<br><br>"
            "I took a lot of photos. These are just a few of them. The trip itself was lovely — equal parts smiles, footsteps, and food. "
            "We wandered all over the city, mostly away from the crowds of Mall Road, discovering side alleys, staircases, and sleepy slopes.<br><br>"
            "One morning, we stumbled upon a tiny local breakfast joint that served something called licchi. It tasted amazing. Like nothing we’d had before "
            "(okay, that might be an exaggeration). Was it actually that good, or were we just extremely hungry? "
            "No idea. What I do know is I’d go back just to try and find that place again. Totally worth the effort — or at least the romantic quest of it.<br><br>"
            "Fun fact: Shimla was once the summer capital of British India, and its architecture still carries colonial leftovers in red roofs and stone walls. "
            "The Kalka–Shimla Railway is a UNESCO World Heritage Site — and also the place where we spent a solid 7 hours stranded one night. "
            "Not by accident. We chose to. (Read: I misplanned the connecting train from Delhi to Kalka. We arrived <em>slightly</em> ahead of schedule.) "
            "It was oddly magical. I now have enough visual content from Kalka station to make a short film about it.<br><br>"
            "Shimla sits in the southwestern Himalayas at an average altitude of 2,206 metres (7,238 ft) — high enough for pleasant summer weather, "
            "but low enough that you don’t need a jacket. Beyond Lower Bazaar and the usual loops, we also climbed the long stairway to Jakhu Mandir "
            "and drove out to the Himalayan Nature Park in Kufri.<br><br>"
            "It’s hard to say what I loved more — the walking, the company, or the memories (read pictures) that came home with me."
        )
    },
    {
        "folder": "harshil",
        "title": "Harshil, 2024",
        "description": (
            "After Shimla, I went on a trip to Harshil with my parents. There were other stops along the way, "
            "but Harshil was the main event — the headliner, if you will.<br><br>"
            "Unlike Shimla, which leans heavily into its touristy charm, Harshil is refreshingly under the radar — "
            "the kind of place that travel influencers would call <em>“undiscovered”</em> just before ruining it.<br><br>"
            "This was also my third and final trip with my beloved Fujifilm XT1 (RIP, old friend). Harshil gave it a worthy send-off.<br><br>"
            "The valley, tucked near the India–China border, wraps around you with pine-covered hills and silence. "
            "We stayed in a village apple orchard where the Bhagirathi river flowed just a few feet from where we slept. "
            "It felt like living inside a postcard.<br><br>"
            "Tourism here is still in its awkward teenage phase — a few shops have popped up selling everything from "
            "woolens to Maggi, but it hasn't yet gone full 'Mall Road.' I kept wondering: is this good?<br><br>"
            "On one hand, more visitors mean more money for locals — a new shop here, a homestay there. "
            "But does it also mean something quiet and unspoiled is slowly being traded in for something louder and shinier? "
            "Probably both.<br><br>"
            "As with most change, it’s complicated. New roads bring new routes and new risks. "
            "But also, more people get to fall in love with places like this — like I did."
        )
    }
]


HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Photos – Kavya Agarwal</title>
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
  <nav>
    <h2><a href="index.html">Kavya Agarwal</a></h2>
    <ul>
      <li><a href="about.html">About</a></li>
      <li><a href="essays.html">Essays</a></li>
      <li><a href="photos.html">Photos</a></li>
      <li><a href="lifelist.html">Life List</a></li>
    </ul>
  </nav>

  <main>
    <h1>Photos</h1>
"""

FOOTER = """  </main>
</body>
</html>
"""

def generate_html():
    with open(OUTPUT_FILE, "w") as f:
        f.write(HEADER)

        for trip in TRIPS:
            folder_path = os.path.join(PHOTO_ROOT, trip["folder"])
            images = sorted([
                img for img in os.listdir(folder_path)
                if os.path.splitext(img)[1].lower() in IMAGE_EXTENSIONS
            ])

            # Write section header
            f.write(f'<section>\n<h2>{trip["title"]}</h2>\n<p>{trip["description"]}</p>\n<div class="photo-grid">\n')

            # Write images
            for img in images:
                src = f'{PHOTO_ROOT}/{trip["folder"]}/{img}'
                f.write(f'  <img src="{src}" alt="{img}">\n')

            f.write("</div>\n</section>\n\n")

        f.write(FOOTER)

    print(f"✅ Updated {OUTPUT_FILE} with {len(TRIPS)} trip sections.")

if __name__ == "__main__":
    generate_html()
