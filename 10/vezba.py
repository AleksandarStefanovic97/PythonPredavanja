from methods import load_file, save_file


data = load_file("data/products.json")

print(data)

data.append({
    "name": "Test test"
})

save_file("data/user.json", data)

