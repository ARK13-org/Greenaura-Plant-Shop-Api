
from pathlib import Path

from app.database.connection import SessionLocal
from app.models.category_model import Category
from app.models.plant_model import Plant


# Project root / uploads / plants
UPLOAD_DIR = Path(__file__).resolve().parent.parent / "uploads" / "plants"

CATEGORIES = [
    "Indoor Plants",
    "Succulents",
    "Flowering Plants",
    "Air Purifying Plants",
]


# Price is in USD.
# Temperature is in Celsius.
# Humidity is a percentage.
# Ratings are illustrative demo catalogue ratings.

PLANTS = [
    # --------------------------------------------------
    # EXISTING 8 PLANTS
    # --------------------------------------------------
    {
        "plant_name": "Aloe Vera",
        "category": "Succulents",
        "price": 12.99,
        "size": "Small (20-30 cm)",
        "rating": 4.7,
        "humidity": 35,
        "temperature": 24,
        "image_url": "/uploads/plants/aloe-vera.png",
        "description": (
            "A popular succulent with thick, fleshy leaves that store water. "
            "Aloe Vera prefers bright indirect light or gentle direct sunlight "
            "and well-draining soil. Allow the soil to dry completely between "
            "waterings. It is well suited to sunny windowsills."
        ),
    },
    {
        "plant_name": "Calathea Orbifolia",
        "category": "Indoor Plants",
        "price": 34.99,
        "size": "Medium (40-60 cm)",
        "rating": 4.8,
        "humidity": 70,
        "temperature": 22,
        "image_url": "/uploads/plants/calathea-orbifolia.png",
        "description": (
            "Known for its large, rounded leaves with distinctive silver-green "
            "stripes. Calathea Orbifolia prefers bright indirect light, "
            "consistently lightly moist soil, and high humidity. Avoid direct "
            "sunlight and cold drafts."
        ),
    },
    {
        "plant_name": "Fiddle Leaf Fig",
        "category": "Indoor Plants",
        "price": 49.99,
        "size": "Large (80-120 cm)",
        "rating": 4.6,
        "humidity": 55,
        "temperature": 23,
        "image_url": "/uploads/plants/fidel-leaf-plant.png",
        "description": (
            "A striking indoor tree with large, violin-shaped leaves. "
            "Fiddle Leaf Fig grows best in bright indirect light and stable "
            "temperatures. Water when the upper soil has started to dry, "
            "and avoid moving it frequently."
        ),
    },
    {
        "plant_name": "Jade Plant",
        "category": "Succulents",
        "price": 18.99,
        "size": "Small (20-35 cm)",
        "rating": 4.7,
        "humidity": 35,
        "temperature": 22,
        "image_url": "/uploads/plants/jade-plant.png",
        "description": (
            "A long-lived succulent with thick oval leaves and woody stems. "
            "Jade Plants enjoy bright light, several hours of gentle sunlight, "
            "and well-draining soil. Water thoroughly but infrequently."
        ),
    },
    {
        "plant_name": "Peace Lily",
        "category": "Flowering Plants",
        "price": 27.99,
        "size": "Medium (35-55 cm)",
        "rating": 4.8,
        "humidity": 65,
        "temperature": 22,
        "image_url": "/uploads/plants/peace-plant.png",
        "description": (
            "A graceful tropical plant with glossy green leaves and elegant "
            "white flower-like spathes. Peace Lilies prefer indirect light, "
            "warm conditions, and evenly moist soil. They appreciate higher "
            "humidity and should be protected from cold drafts."
        ),
    },
    {
        "plant_name": "Rubber Plant",
        "category": "Indoor Plants",
        "price": 32.99,
        "size": "Medium (50-80 cm)",
        "rating": 4.7,
        "humidity": 50,
        "temperature": 23,
        "image_url": "/uploads/plants/rubber-plant.png",
        "description": (
            "Ficus elastica is admired for its thick, glossy leaves and upright "
            "growth. It prefers bright indirect light but tolerates moderate "
            "light. Allow the top layer of soil to dry before watering."
        ),
    },
    {
        "plant_name": "Snake Plant",
        "category": "Air Purifying Plants",
        "price": 24.99,
        "size": "Medium (40-65 cm)",
        "rating": 4.9,
        "humidity": 35,
        "temperature": 23,
        "image_url": "/uploads/plants/snake-plant.png",
        "description": (
            "A resilient plant with upright, sword-shaped leaves. Snake Plants "
            "tolerate a wide range of indoor light conditions and prefer soil "
            "that dries between waterings. Avoid overwatering, especially "
            "during cooler months."
        ),
    },
    {
        "plant_name": "ZZ Plant",
        "category": "Air Purifying Plants",
        "price": 29.99,
        "size": "Medium (40-60 cm)",
        "rating": 4.9,
        "humidity": 40,
        "temperature": 23,
        "image_url": "/uploads/plants/zz-plant.png",
        "description": (
            "Zamioculcas zamiifolia has shiny, deep-green leaves and thick "
            "underground rhizomes that store water. It tolerates low light "
            "and infrequent watering. Let the soil dry thoroughly before "
            "watering again."
        ),
    },

    # --------------------------------------------------
    # 30 NEW PLANTS
    # --------------------------------------------------
    {
        "plant_name": "Maidenhair Fern",
        "category": "Indoor Plants",
        "price": 22.99,
        "size": "Small (25-35 cm)",
        "rating": 4.6,
        "humidity": 75,
        "temperature": 21,
        "image_url": "/uploads/plants/maidenhair-fern-plant.png",
        "description": (
            "A delicate fern with fine, fan-shaped leaflets and dark stems. "
            "It needs high humidity, gentle indirect light, and consistently "
            "moist soil. Avoid letting the root ball dry out."
        ),
    },
    {
        "plant_name": "Lavender",
        "category": "Flowering Plants",
        "price": 16.99,
        "size": "Small (25-40 cm)",
        "rating": 4.7,
        "humidity": 40,
        "temperature": 22,
        "image_url": "/uploads/plants/lavender-plant.png",
        "description": (
            "A fragrant Mediterranean plant with narrow silvery-green leaves "
            "and purple flower spikes. Lavender needs abundant direct sunlight, "
            "good airflow, and sharply draining soil. Allow the soil to dry "
            "between waterings."
        ),
    },
    {
        "plant_name": "Kentia Palm",
        "category": "Indoor Plants",
        "price": 59.99,
        "size": "Large (90-130 cm)",
        "rating": 4.8,
        "humidity": 55,
        "temperature": 22,
        "image_url": "/uploads/plants/kentia-palm-plant.png",
        "description": (
            "A graceful palm with arching, feather-like fronds. Kentia Palms "
            "adapt well to bright indirect light and can tolerate lower light. "
            "Water when the upper soil begins to dry and avoid waterlogged roots."
        ),
    },
    {
        "plant_name": "Kalanchoe",
        "category": "Flowering Plants",
        "price": 17.99,
        "size": "Small (20-30 cm)",
        "rating": 4.6,
        "humidity": 40,
        "temperature": 22,
        "image_url": "/uploads/plants/kalanchoe-plant.png",
        "description": (
            "A compact succulent known for clusters of long-lasting flowers "
            "in bright colors. Kalanchoe prefers bright light and well-draining "
            "soil. Water only after the soil has mostly dried."
        ),
    },
    {
        "plant_name": "Dracaena",
        "category": "Air Purifying Plants",
        "price": 31.99,
        "size": "Medium (60-90 cm)",
        "rating": 4.6,
        "humidity": 45,
        "temperature": 23,
        "image_url": "/uploads/plants/dracaena-plant.png",
        "description": (
            "A popular tropical foliage plant with upright stems and long, "
            "often variegated leaves. Dracaena prefers filtered light and "
            "moderate watering. Let the top layer of soil dry before watering."
        ),
    },
    {
        "plant_name": "Dieffenbachia",
        "category": "Indoor Plants",
        "price": 26.99,
        "size": "Medium (45-70 cm)",
        "rating": 4.5,
        "humidity": 60,
        "temperature": 22,
        "image_url": "/uploads/plants/dieffenbachia-plant.png",
        "description": (
            "A tropical foliage plant with broad green leaves patterned "
            "with creamy white markings. It grows best in bright indirect "
            "light, warm temperatures, and lightly moist soil. Keep away "
            "from pets and children because its sap is toxic."
        ),
    },
    {
        "plant_name": "Bonsai Tree",
        "category": "Indoor Plants",
        "price": 44.99,
        "size": "Small (25-40 cm)",
        "rating": 4.8,
        "humidity": 50,
        "temperature": 21,
        "image_url": "/uploads/plants/bonsai-plant.png",
        "description": (
            "A carefully cultivated miniature tree that brings a sculptural "
            "look to a room. Bonsai care depends on the species. Provide "
            "appropriate light, regular pruning, and careful watering; do not "
            "allow the root system to dry out completely."
        ),
    },
    {
        "plant_name": "Banana Plant",
        "category": "Indoor Plants",
        "price": 39.99,
        "size": "Large (70-110 cm)",
        "rating": 4.5,
        "humidity": 65,
        "temperature": 25,
        "image_url": "/uploads/plants/banana_plant.png",
        "description": (
            "A tropical plant with large, broad leaves that create a lush "
            "statement indoors. Banana Plants need bright light, warmth, "
            "regular watering, and higher humidity. Give the leaves room "
            "to spread."
        ),
    },
    {
        "plant_name": "Gardenia",
        "category": "Flowering Plants",
        "price": 28.99,
        "size": "Medium (35-50 cm)",
        "rating": 4.7,
        "humidity": 65,
        "temperature": 21,
        "image_url": "/uploads/plants/gardenia-plant_nobg.png",
        "description": (
            "A fragrant evergreen shrub with glossy leaves and creamy white "
            "flowers. Gardenias prefer bright indirect light, acidic "
            "well-draining soil, high humidity, and evenly moist conditions. "
            "Avoid sudden changes in temperature."
        ),
    },
    {
        "plant_name": "Bird of Paradise",
        "category": "Indoor Plants",
        "price": 69.99,
        "size": "Large (100-150 cm)",
        "rating": 4.8,
        "humidity": 55,
        "temperature": 24,
        "image_url": "/uploads/plants/bird-of-paradis-plant.png",
        "description": (
            "A dramatic tropical plant with large, paddle-shaped leaves. "
            "Bird of Paradise grows best in very bright light, warm conditions, "
            "and well-draining soil. Rotate the pot occasionally for balanced "
            "growth."
        ),
    },
    {
        "plant_name": "Chinese Evergreen",
        "category": "Air Purifying Plants",
        "price": 25.99,
        "size": "Medium (35-55 cm)",
        "rating": 4.7,
        "humidity": 55,
        "temperature": 22,
        "image_url": "/uploads/plants/chinese-evergreen-plant.png",
        "description": (
            "Aglaonema is valued for its patterned foliage and tolerance "
            "of indoor conditions. It prefers indirect light, warm "
            "temperatures, and soil that is allowed to partly dry between "
            "waterings. Keep away from pets because it is toxic if ingested."
        ),
    },
    {
        "plant_name": "Dwarf Umbrella Tree",
        "category": "Indoor Plants",
        "price": 29.99,
        "size": "Medium (45-70 cm)",
        "rating": 4.5,
        "humidity": 50,
        "temperature": 22,
        "image_url": "/uploads/plants/dwarf-dmbrella-plant.png",
        "description": (
            "Schefflera arboricola has glossy leaflets arranged like the "
            "spokes of an umbrella. It prefers bright indirect light and "
            "moderate watering. Pruning helps maintain a compact shape."
        ),
    },
    {
        "plant_name": "Nerve Plant",
        "category": "Indoor Plants",
        "price": 15.99,
        "size": "Small (10-20 cm)",
        "rating": 4.6,
        "humidity": 75,
        "temperature": 22,
        "image_url": "/uploads/plants/nerve-plant.png",
        "description": (
            "Fittonia is a compact tropical plant with striking contrasting "
            "veins across its leaves. It enjoys high humidity, warm conditions, "
            "and bright filtered light. Keep its soil lightly moist."
        ),
    },
    {
        "plant_name": "Rosemary",
        "category": "Indoor Plants",
        "price": 14.99,
        "size": "Small (20-30 cm)",
        "rating": 4.5,
        "humidity": 40,
        "temperature": 21,
        "image_url": "/uploads/plants/rosemary-plant-no-bg.png",
        "description": (
            "A fragrant Mediterranean herb with needle-like leaves. Rosemary "
            "needs several hours of direct sunlight, excellent drainage, "
            "and good airflow. Allow the soil to dry somewhat between "
            "waterings."
        ),
    },
    {
        "plant_name": "Spider Plant",
        "category": "Air Purifying Plants",
        "price": 19.99,
        "size": "Medium (25-40 cm)",
        "rating": 4.8,
        "humidity": 50,
        "temperature": 22,
        "image_url": "/uploads/plants/spider-plant.png",
        "description": (
            "A forgiving plant with arching striped leaves and dangling "
            "plantlets. Spider Plants prefer bright indirect light and "
            "moderate watering. Allow excess water to drain freely."
        ),
    },
    {
        "plant_name": "Weeping Fig",
        "category": "Indoor Plants",
        "price": 42.99,
        "size": "Large (80-120 cm)",
        "rating": 4.5,
        "humidity": 50,
        "temperature": 22,
        "image_url": "/uploads/plants/weeping-fig-plant.png",
        "description": (
            "Ficus benjamina is a graceful indoor tree with slender branches "
            "and small glossy leaves. It prefers bright filtered light, "
            "consistent watering, and a stable position. Avoid sudden "
            "environmental changes."
        ),
    },
    {
        "plant_name": "Hoya Carnosa",
        "category": "Flowering Plants",
        "price": 24.99,
        "size": "Medium (25-45 cm)",
        "rating": 4.8,
        "humidity": 55,
        "temperature": 22,
        "image_url": "/uploads/plants/hoya-carson-plant.png",
        "description": (
            "A trailing tropical vine with thick waxy leaves and clusters "
            "of star-shaped flowers. Hoya Carnosa prefers bright indirect "
            "light and well-draining soil. Let the soil dry between waterings."
        ),
    },
    {
        "plant_name": "African Violet",
        "category": "Flowering Plants",
        "price": 18.99,
        "size": "Small (15-25 cm)",
        "rating": 4.7,
        "humidity": 55,
        "temperature": 22,
        "image_url": "/uploads/plants/african-violet.png",
        "description": (
            "A compact flowering plant with soft leaves and colorful blooms. "
            "African Violets prefer bright indirect light and evenly moist "
            "soil. Avoid cold water on the leaves and provide gentle airflow."
        ),
    },
    {
        "plant_name": "Tradescantia",
        "category": "Indoor Plants",
        "price": 16.99,
        "size": "Small (20-30 cm)",
        "rating": 4.6,
        "humidity": 50,
        "temperature": 22,
        "image_url": "/uploads/plants/tradescantia-plant_nobg.png",
        "description": (
            "A colorful trailing plant with patterned foliage in shades "
            "of green, purple, and silver. Tradescantia grows well in bright "
            "indirect light and moderately moist, well-draining soil. Pinch "
            "back stems to encourage fuller growth."
        ),
    },
    {
        "plant_name": "Venus Flytrap",
        "category": "Indoor Plants",
        "price": 21.99,
        "size": "Small (10-15 cm)",
        "rating": 4.7,
        "humidity": 60,
        "temperature": 22,
        "image_url": "/uploads/plants/venus-flytrap-plant_nobg.png",
        "description": (
            "A fascinating carnivorous plant with hinged traps that catch "
            "small insects. Venus Flytraps need several hours of direct "
            "sunlight, mineral-free water such as rainwater, and nutrient-poor "
            "peat-based growing medium. Never use ordinary potting soil."
        ),
    },
    {
        "plant_name": "Prayer Plant",
        "category": "Indoor Plants",
        "price": 23.99,
        "size": "Small (20-30 cm)",
        "rating": 4.8,
        "humidity": 65,
        "temperature": 22,
        "image_url": "/uploads/plants/prayer-plant_nobg.png",
        "description": (
            "Maranta leuconeura has beautifully patterned leaves that fold "
            "upward at night. It prefers bright indirect light, warm conditions, "
            "high humidity, and consistently lightly moist soil."
        ),
    },
    {
        "plant_name": "Echeveria",
        "category": "Succulents",
        "price": 13.99,
        "size": "Small (10-15 cm)",
        "rating": 4.8,
        "humidity": 35,
        "temperature": 23,
        "image_url": "/uploads/plants/echeveria-plant_nobg.png",
        "description": (
            "A rosette-forming succulent with fleshy leaves in attractive "
            "green, blue, or pink tones. Echeveria needs bright light, "
            "well-draining succulent soil, and infrequent watering. Keep "
            "water away from the center of the rosette."
        ),
    },
    {
        "plant_name": "Croton",
        "category": "Indoor Plants",
        "price": 27.99,
        "size": "Medium (40-60 cm)",
        "rating": 4.5,
        "humidity": 60,
        "temperature": 24,
        "image_url": "/uploads/plants/croton-plant_nobg.png",
        "description": (
            "A colorful tropical foliage plant with leaves marked in red, "
            "orange, yellow, and green. Crotons need bright light to maintain "
            "their colors, warm temperatures, and evenly moist soil. Avoid "
            "cold drafts and sudden changes."
        ),
    },
    {
        "plant_name": "Staghorn Fern",
        "category": "Indoor Plants",
        "price": 35.99,
        "size": "Medium (35-50 cm)",
        "rating": 4.7,
        "humidity": 70,
        "temperature": 22,
        "image_url": "/uploads/plants/staghorn-fern-plant.png",
        "description": (
            "An unusual epiphytic fern with antler-shaped fronds and "
            "shield-like basal leaves. It prefers bright indirect light, "
            "good airflow, and humid conditions. Water when its growing "
            "medium begins to dry."
        ),
    },
    {
        "plant_name": "Polka Dot Plant",
        "category": "Indoor Plants",
        "price": 14.99,
        "size": "Small (15-25 cm)",
        "rating": 4.5,
        "humidity": 60,
        "temperature": 22,
        "image_url": "/uploads/plants/polka-dot-plant.png",
        "description": (
            "Hypoestes phyllostachya is a compact plant with colorful "
            "speckled leaves. It prefers bright indirect light, warm "
            "conditions, and evenly moist soil. Pinch growing tips to "
            "encourage a bushier shape."
        ),
    },
    {
        "plant_name": "Peperomia",
        "category": "Indoor Plants",
        "price": 20.99,
        "size": "Small (15-25 cm)",
        "rating": 4.7,
        "humidity": 45,
        "temperature": 22,
        "image_url": "/uploads/plants/peperomia-plant.png",
        "description": (
            "A compact tropical foliage plant with thick leaves and many "
            "attractive varieties. Peperomia prefers bright indirect light "
            "and an airy, well-draining potting mix. Let the soil partly "
            "dry before watering."
        ),
    },
    {
        "plant_name": "Olive Tree",
        "category": "Indoor Plants",
        "price": 54.99,
        "size": "Large (70-100 cm)",
        "rating": 4.6,
        "humidity": 40,
        "temperature": 22,
        "image_url": "/uploads/plants/olive-tree-plant.png",
        "description": (
            "An elegant Mediterranean tree with narrow silvery-green leaves. "
            "Olive Trees need abundant direct sunlight, excellent drainage, "
            "and careful watering. Indoors, place it beside the brightest "
            "available window."
        ),
    },
    {
        "plant_name": "Norfolk Island Pine",
        "category": "Indoor Plants",
        "price": 38.99,
        "size": "Medium (50-80 cm)",
        "rating": 4.6,
        "humidity": 55,
        "temperature": 20,
        "image_url": "/uploads/plants/norka-island-pine-plant.png",
        "description": (
            "A symmetrical evergreen with soft, tiered branches that resemble "
            "a miniature Christmas tree. Norfolk Island Pine prefers bright "
            "indirect light, moderate humidity, and evenly moist but well-drained "
            "soil. Protect it from dry air."
        ),
    },
    {
        "plant_name": "Moth Orchid",
        "category": "Flowering Plants",
        "price": 36.99,
        "size": "Medium (30-50 cm)",
        "rating": 4.9,
        "humidity": 60,
        "temperature": 23,
        "image_url": "/uploads/plants/moth-orchid-plant.png",
        "description": (
            "Phalaenopsis is an elegant orchid known for long-lasting flowers "
            "on arching stems. It prefers bright indirect light, warm "
            "temperatures, and an airy orchid-bark growing medium. Water "
            "when the roots turn silvery and the medium begins to dry."
        ),
    },
    {
        "plant_name": "Monstera",
        "category": "Indoor Plants",
        "price": 39.99,
        "size": "Large (60-90 cm)",
        "rating": 4.9,
        "humidity": 60,
        "temperature": 24,
        "image_url": "/uploads/plants/monstres-plant.png",
        "description": (
            "A tropical climbing plant with large, naturally split leaves "
            "as it matures. Monstera prefers bright indirect light, warm "
            "conditions, and a chunky, well-draining soil mix. Provide a "
            "support pole as it grows."
        ),
    },
]


def seed_database():
    db = SessionLocal()

    try:
        print("\nStarting GreenAura database seeding...")

        # 1. Validate every image before modifying the database.
        missing_images = []

        for plant_data in PLANTS:
            image_name = Path(plant_data["image_url"]).name
            image_path = UPLOAD_DIR / image_name

            if not image_path.is_file():
                missing_images.append(image_name)

        if missing_images:
            print("\nERROR: The following plant images are missing:")

            for image_name in missing_images:
                print(f"  - {image_name}")

            print(
                "\nCopy all missing images into uploads/plants "
                "and run the seed command again."
            )
            return

        print(f"Validated {len(PLANTS)} plant images.")

        # 2. Create missing categories.
        category_objects = {}

        for category_name in CATEGORIES:
            category = (
                db.query(Category)
                .filter(Category.name == category_name)
                .first()
            )

            if category is None:
                category = Category(name=category_name)
                db.add(category)
                db.flush()

                print(f"Created category: {category_name}")

            category_objects[category_name] = category

        # 3. Create or update plants.
        created_count = 0
        updated_count = 0

        for plant_data in PLANTS:
            data = plant_data.copy()
            category_name = data.pop("category")

            category = category_objects[category_name]

            plant = (
                db.query(Plant)
                .filter(Plant.plant_name == data["plant_name"])
                .first()
            )

            if plant is None:
                plant = Plant(
                    **data,
                    category_id=category.id,    
            )

                db.add(plant)
                created_count += 1

                print(f"Added: {data['plant_name']}")

            else:
                for key, value in data.items():
                    setattr(plant, key, value)

                plant.category_id = category.id
                updated_count += 1

                print(f"Updated: {data['plant_name']}")

        # 4. Commit all changes.
        db.commit()

        total_plants = db.query(Plant).count()
        total_categories = db.query(Category).count()

        print("\nGreenAura database seeding completed!")
        print("--------------------------------------")
        print(f"New plants added: {created_count}")
        print(f"Existing plants updated: {updated_count}")
        print(f"Total plants in database: {total_plants}")
        print(f"Total categories in database: {total_categories}")

    except Exception as error:
        db.rollback()
        print(f"\nSeeding failed: {error}")
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
