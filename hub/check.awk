BEGIN{
	
	FS="\t";
	found="false";

}
{
	if($1 ~ usr)
	{found="true";
	
	}
}
END{
print found;
}

