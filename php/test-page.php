<style type="text/css">
	a{
		margin: 5px;
	}
	.active {
		color: red;
	}
	.page {
		background-color: #f0f0f0;
	}
</style>
<?php
require_once './pagination.php';
Pagination::$total = 10001;
Pagination::$index = 1;
Pagination::$row   = 10;

?>
<div id="page">
	<?php echo Pagination2::page(); ?>
</div>
<script src="http://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>
<script type="text/javascript">
	$('body').on('click', 'a',function(event) {
		var total_page = <?php echo ceil(Pagination::$total / Pagination::$row); ?>;
		var cd = $(this).text();
		var active = $('.active').text();
		cd = parseInt(cd);
		active = parseInt(active);

		if ($(this).hasClass('first')) {
			cd = 1;
		}else if ($(this).hasClass('deduct')) {
			cd = active - 1;
		}else if ($(this).hasClass('add')) {
			cd = active +1;
		}else if($(this).hasClass('last')) {
			cd = total_page;
		}

		$.ajax({
			type:'post',
			url:'./ajax.php',
			data:{'cd':cd},
			dataType:'html',
			success:function(ret) {
				$('#page').empty().html(ret);
			}
		});
	})
</script>