<?php
$everything = get_defined_vars();
ksort($everything);
echo '<pre>';
print_r($everything);
echo '</pre>';
?>