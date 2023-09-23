def linear_search_product(product_list, target_product):
    indices = []
    
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    
    return indices

def main():
    # Input list of products
    products = ["apple", "banana", "apple", "orange", "apple"]
    
    # Input target product to search for
    target = input("Enter the product name to search for: ")
    
    # Call the linear_search_product function
    result = linear_search_product(products, target)
    
    # Display the result
    if result:
        print(f"The product '{target}' was found at indices: {result}")
    else:
        print(f"The product '{target}' was not found in the list.")

if __name__ == "__main__":
    main()