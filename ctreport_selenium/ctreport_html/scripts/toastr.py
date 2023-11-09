content = '''
<script>
		function toast_message(status) {
		
			toastr.options = {
				"closeButton": false,
				"debug": false,
				"newestOnTop": false,
				"progressBar": false,
				"positionClass": "toast-bottom-right",
				"preventDuplicates": false,
				"onclick": null,
				"showDuration": "300",
				"hideDuration": "400",
				"timeOut": "5000",
				"extendedTimeOut": "1000",
				"showEasing": "swing",
				"hideEasing": "linear",
				"showMethod": "fadeIn",
				"hideMethod": "fadeOut"
			};
			if(status=="all")
			{
				toastr["info"]("Filter Removed");
			}
			else{
			toastr["info"]("Filtered "+status.replace(/^./, status[0].toUpperCase())+" Test Cases");
			}
		};
	</script>
'''
