
from app.database.connection import SessionLocal
from app.models.category_model import Category
from app.models.plant_model import Plant


PLANTS_TO_REMOVE = [
    "Monstera Deliciosa",
    "aaa",
    "Golden Pothos",
    "Echeveria",
    "Areca Palm",
]

CATEGORY_TO_REMOVE = "a"


def cleanup_database():
    db = SessionLocal()

    try:
        print("\nStarting GreenAura database cleanup...")

        # 1. Find and delete unwanted plants.
        deleted_plants = 0

        for plant_name in PLANTS_TO_REMOVE:
            plant = (
                db.query(Plant)
                .filter(Plant.plant_name == plant_name)
                .first()
            )

            if plant:
                db.delete(plant)
                deleted_plants += 1
                print(f"Deleted plant: {plant_name}")
            else:
                print(f"Not found (already removed): {plant_name}")

        # Flush deletions before checking category usage.
        db.flush()

        # 2. Remove test category only if it is unused.
        category = (
            db.query(Category)
            .filter(Category.name == CATEGORY_TO_REMOVE)
            .first()
        )

        if category:
            remaining_plants = (
                db.query(Plant)
                .filter(Plant.category_id == category.id)
                .count()
            )

            if remaining_plants == 0:
                db.delete(category)
                print(f"Deleted unused category: {CATEGORY_TO_REMOVE}")
            else:
                print(
                    f"Keeping category '{CATEGORY_TO_REMOVE}': "
                    f"{remaining_plants} plants still use it."
                )

        # 3. Save changes.
        db.commit()

        print("\nCleanup completed successfully!")
        print(f"Plants deleted: {deleted_plants}")
        print(f"Remaining plants: {db.query(Plant).count()}")
        print(f"Remaining categories: {db.query(Category).count()}")

    except Exception as error:
        db.rollback()
        print(f"\nCleanup failed: {error}")
        print("All cleanup changes have been rolled back.")
        raise

    finally:
        db.close()


if __name__ == "__main__":
    cleanup_database()
