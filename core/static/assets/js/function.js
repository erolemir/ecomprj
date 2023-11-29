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

$(".delete-product").on("click", function () {
    
    let product_id = $(this).attr("data-product");
    let this_val = $(this);

    console.log("Product ID: ", product_id);

    $.ajax({
        url: "/delete-from-cart",
        data: {
            "id": product_id,
        },
        dataType: "json",
        beforeSend : function(){
            this_val.hide();
        },
        success: function(response){
            this_val.show();
            $(".cart-items-count").text(response.totalcartitems);
            $("#cart-list").html(response.data);
        },
    });
});

$(".update-product").on("click", function () {
    
    let product_id = $(this).attr("data-product");
    let this_val = $(this);
    let product_quantity = $(".product-qty-" + product_id).val();

    console.log("Product ID: ", product_id);

    $.ajax({
        url: "/update-cart",
        data: {
            "id": product_id,
            "qty": product_quantity,
        },
        dataType: "json",
        beforeSend : function(){
            this_val.hide();
        },
        success: function(response){
            this_val.show();
            $(".cart-items-count").text(response.totalcartitems);
            $("#cart-list").html(response.data);
        },
    });
});

$(document).on("submit","#contact-form-ajax",function(e){
    e.preventDefault();
    console.log("Form Gönderildi");
    let full_name = $("#full_name").val();
    let email = $("#email").val();
    let subject = $("#subject").val();
    let phone = $("#phone").val();
    let message = $("#message").val();

    console.log("Full Name: ", full_name);
    console.log("Email: ", email);
    console.log("Subject: ", subject);
    console.log("Phone: ", phone);
    console.log("Message: ", message);

    $.ajax({
        url: "/ajax-contact-form",
        data: {
            "full_name": full_name,
            "email": email,
            "subject": subject,
            "phone": phone,
            "message": message,
        },
        dataType: "json",
        beforeSend : function(){
           console.log("Form Gönderiliyor");
        },
        success: function(response){
            console.log("Form Gönderildi");
            $("#contact-form-ajax").hide();
            $("#contact-form-ajax").html("<h3>Teşekkürler! Form başarıyla gönderildi.</h3>");
            $("#contact-form-ajax").show();
        },
    });
});