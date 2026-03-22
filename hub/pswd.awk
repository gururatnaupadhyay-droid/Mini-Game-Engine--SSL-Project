BEGIN{
FS="\t";
}

{
if($1 ~ usr)
{print $2;
}
}
