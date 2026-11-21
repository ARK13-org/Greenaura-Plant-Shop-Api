# GreenAura integration package

This package combines your supplied Flutter UI, assets, pubspec and FastAPI backend. Existing visual screens and plant catalogue data are retained. The integration adds server-side plant search/category filtering, plant-detail refresh, account registration/login, JWT sessions and per-user persistent favorites.

## 1. Backend setup (PowerShell)

Open a terminal in `Backend` (or copy its contents into your existing backend folder). Keep your existing `greenaura.db` and full `uploads` folder beside `app/`.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:SECRET_KEY = "replace-with-a-long-random-secret"
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

If you already have a working `.venv`, activate it and run only `pip install -r requirements.txt` plus the environment variable and Uvicorn commands. `Base.metadata.create_all()` creates the new `user_favorites` table without deleting existing plants/categories/users.

Open `http://127.0.0.1:8000/docs` to inspect the API.

## 2. Flutter setup

Merge the contents of the `Flutter` folder into your existing Flutter project root (the folder that already contains your `android`, `web`, `ios`, or other platform folders). Replace its `lib/`, `assets/`, and `pubspec.yaml` with the supplied versions; keep your existing native/platform folders and project configuration. Then run:

```powershell
flutter pub get
flutter run -d chrome --web-port 2350
```

For an Android emulator, use:

```powershell
flutter run --dart-define=API_HOST=10.0.2.2:8000
```

For a physical Android device, replace the host with your computer's LAN IP and make sure both devices share the same network. The API host defaults to `127.0.0.1:8000` for local Chrome development.

## 3. Integrated features

- Plant catalogue: `GET /plants/`
- Plant detail: `GET /plants/{plant_id}`
- Search: `GET /plants/?search=fern`
- Category filter: `GET /plants/?category_id=2`
- Combined filter: `GET /plants/?search=fern&category_id=2`
- Categories: `GET /category`
- Registration: `POST /user`
- Login: `POST /auth/login` (form fields `username`, `password`)
- Current account: `GET /auth/me` (Bearer token)
- Update account details: `PATCH /user/me` (Bearer token)
- Favorites list: `GET /user/me/favorites` (Bearer token)
- Add/remove favorite: `PUT /plants/{plant_id}/favorite` with `{"is_favorite": true|false}`

Flutter persists the access token with `shared_preferences`. For production, use secure platform storage and a strong secret key supplied through environment configuration. Do not commit `.env` or real secrets.

## 4. Important notes

- Login uses `username` plus password, matching the backend's existing user schema.
- Existing `POST /user` registration and profile-picture endpoint are retained.
- Profile name/email editing is connected through `PATCH /user/me`. Address book, orders, notifications, checkout/payment, and plant scanning remain UI placeholders because the supplied backend does not define those features/endpoints.
- Favorites now require sign-in; the app prompts the user if they tap a favorite while signed out.
- The uploaded archives did not include the full Android/iOS/Web platform folders, the original SQLite database, or the full backend image upload folder. Merge the supplied Flutter files into your existing Flutter project rather than replacing its platform folders. Keep your existing database and backend uploads folder.
- Flutter/Dart SDK is not installed in this execution environment, so a local `flutter analyze`/build could not be run here. Run `flutter pub get` and `flutter analyze` in your own VS Code terminal after extracting.
