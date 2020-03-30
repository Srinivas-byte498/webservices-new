(function() {
    $("#existingUserLogin").hide();
    $("#newUserLogin").hide();
    $("#loginSubmit").hide();
    $('#userMobileNumber').parsley().on('field:success', function() {

        dataObj={
            "phonenumber": $('#userMobileNumber').val()
        }
       
        $.post("http://localhost:8000/clients/registration/validate-phoneno", JSON.stringify(dataObj), function(res){
            data = res.data;
            $("#loginSubmit").show();
            if(res.statusCode == 0){
                $('.invalid-form-error-message')
                    .html('')
                    .toggleClass('filled', false);
                
                if(data){
                    console.log("old");
                    $("#newUserLogin").hide();
                    $("#existingUserLogin").show();  
                }else{
                    console.log("new");
                    $("#newUserLogin").show();
                    $("#existingUserLogin").hide();  
                }
            }else if(res.statusCode == 1){
                $('.invalid-form-error-message')
                    .html('Internal Server Error, try later')
                    .toggleClass('filled', true);
                
            }
        });
    });

    $('#userMobileNumber').parsley().on('field:error', function() {
        $("#existingUserLogin").hide();
        $("#newUserLogin").hide();
        $("#loginSubmit").hide();
        $('.invalid-form-error-message')
        .html('')
        .toggleClass('filled', false);
    });


})();

function verifyUserCredentials(){
    
    phonenumber =  $('#userMobileNumber').val()
    otp=$("#userOTP").val();
    password = $("#userPassword").val();

    
    if(otp != "" && password == ""){
        dataObj={
            "phonenumber":"91"+phonenumber,
            "otp":otp
        }
        
        $.post("http://localhost:8000/clients/registration/verifyOTP", JSON.stringify(dataObj), function(res){
            data = res.data;
            statusCode = res.statusCode;
            if(statusCode==0){
                $('.invalid-form-error-message')
                    .html('')
                    .toggleClass('filled', false);
                
                checkPassword(phonenumber);
            }else{
                  
                console.log("Invalid OTP");
                if(statusCode == 3){
                    $('.invalid-form-error-message')
                    .html('Invalid OTP')
                    .toggleClass('filled', true);
                }else if (statusCode == 1){
                    $('.invalid-form-error-message')
                    .html('Internal Server Error, try later')
                    .toggleClass('filled', true);
                }
            }
        });

   
    }else if(password != "" && otp == ""){
        dataObj={
            "phonenumber":phonenumber,
            "password":password
        }
        
        $.post("http://localhost:8000/clients/registration/validate-password", JSON.stringify(dataObj), function(res){
            data = res.data;
            statusCode = res.statusCode;
            if(statusCode==0){
                
                $('.invalid-form-error-message')
                    .html('')
                    .toggleClass('filled', false);
                
                var dateVar = new Date();
                dateVar.setTime(dateVar.getTime() + (1*24*60*60*1000));
                var expires = "expires="+ dateVar.toUTCString();
                //document.cookie="userName="+phonenumber+";"+expires+";path=/";
                window.location.href = "personal-profile"
            }else{
                console.log("Error in validation")
                if(statusCode == 2){
                    $('.invalid-form-error-message')
                    .html('Invalid Credentials')
                    .toggleClass('filled', true);
                }else if (statusCode == 1){
                    $('.invalid-form-error-message')
                    .html('Internal Server Error, try later')
                    .toggleClass('filled', true);
                }
            }
            
        });


    }
}

function checkPassword(phonenumber){
    
    dataObj = {
        "phonenumber":phonenumber
    }

    $.post("http://localhost:8000/clients/registration/check-password", JSON.stringify(dataObj), function(res){
            data = res.data;
            var dateVar = new Date();
            dateVar.setTime(dateVar.getTime() + (1*24*60*60*1000));
            var expires = "expires="+ dateVar.toUTCString();
            document.cookie="userName="+phonenumber+";"+expires+";path=/";
                
            if(data){
                console.log("alredy registered");
                window.location.href = "personal-profile";     
            }else{
                console.log("new user");
                window.location.href = "save-password/"+phonenumber;
            }
    });
    

}