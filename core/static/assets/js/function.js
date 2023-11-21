// $(".add-to-cart-btn").on("click",function(){
//     let quantity = $("#product-quantity").val();
//     let product_title = $(".product-title").val();
//     let product_id = $(".product-id").val();
//     let product_price = $("#current-product-price").text();
//     let this_val = $(this)

//     console.log("Quantity: " , quantity);
//     console.log("Product Title: " , product_title);
//     console.log("Product ID: " , product_id);
//     console.log("Product Price: " , product_price);
//     console.log("Current Element: " , this_val);

//     $.ajax({
//         url: "/add-to-cart",
//         data: {
//             "id": product_id,
//             "qty": quantity,
//             "title": product_title,
//             "price": product_price,
//         },
//         dataType: "json",
//         beforeSend : function(){
//             this_val.text("Sepete Ekleniyor...");
//         },
//         success: function(response){
//             console.log("Sepete Eklendi");
//             this_val.html("Sepete Eklendi");
//             $(".cart-items-count").text(response.totalcartitems);

//         },
//     })

// });

$(".add-to-cart-btn").on("click", function () {
    let this_val = $(this);
    let index = this_val.data("index");
  
    let quantity = $(".product-quantity-" + index).val();
    let product_title = $(".product-title-" + index).val();
    let product_id = $(".product-id-" + index).val();
    let product_price = $(".current-product-price-" + index).text();
    let product_image = $(".product-image-" + index).val();
  
    console.log("Quantity: ", quantity);
    console.log("Product Title: ", product_title);
    console.log("Product ID: ", product_id);
    console.log("Product Price: ", product_price);
    console.log("Product Image: ", product_image);
    console.log("Index: ", index);
    console.log("Current Element: ", this_val);

  

    $.ajax({
        url: "/add-to-cart",
        data: {
            "id": product_id,
            "image": product_image,
            "qty": quantity,
            "title": product_title,
            "price": product_price,
        },
        dataType: "json",
        beforeSend : function(){
            this_val.text("Sepete Ekleniyor...");
        },
        success: function(response){
            console.log("Sepete Eklendi");
            this_val.html("✓");
            $(".cart-items-count").text(response.totalcartitems);

        },
    })

});