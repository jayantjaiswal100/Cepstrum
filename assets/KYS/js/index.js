document.addEventListener("DOMContentLoaded",
    function(event) {
        var microsoft_authorization_url = $('#microsoft-auth-url').val();
        window.microsoft.login = new window.microsoft.objects.LoginController({
            'authorization_url': microsoft_authorization_url
    });
});
