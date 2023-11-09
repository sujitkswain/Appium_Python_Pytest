content = '''
    <script>
        function createimagemodal(path,cap) {
            var html = '<div id="modalWindow1" class="modal" data-keyboard="false" data-backdrop="static">\
                        <span class="close1" onclick=deletemodal("modalWindow1") data-dismiss="modal">&times;</span>\
                        <img class="modal-content" id="img01" style="max-height: -webkit-fill-available; width: auto;"></img>\
                        <div id="caption"></div>\
                        </div>';
            $("#imagemodal").html(html);
            $("#modalWindow1").modal();
            var modalImg = document.getElementById("img01");
            var captionText = document.getElementById("caption");
            modalImg.src = path;
            captionText.innerHTML = cap;
        }
    </script>
    '''
