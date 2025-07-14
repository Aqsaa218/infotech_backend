from app import create_app  # ✅ correct relative import


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
