def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("We don't know that flavor")
    except ValueError as e:#casting the error 
        print("Error: ", e)
    else:
        print(f"{flavor} chai is served")
    finally:#this execute everytime 
        print("Next customer please")

serve_chai("masala")
serve_chai("unknown")