filename = raw_input("Please enter a filename: ");

	
def parse_arg(args, tags):
	temparg="";
	for arg in args:
		arg=arg.strip(" \n\t\r");
		if len(arg)!=0:
			if arg[0]=="'" and arg[len(arg)-1]=="'": 
				for i in range(0, len(tags)):temparg+="<"+tags[i]+">";
				temparg+=arg[1:-1]
				for i in range(0, len(tags))[::-1]:temparg+="</"+tags[i]+">";
			elif arg[0]=="*": temparg+='<block var="'+arg[1:]+'"/>';
			else: temparg+=convert_command(arg);
	return temparg;
	
def convert_variable(declaration):
	syntax = '<variable name="{}">{}</variable>';
	if "=" in declaration:
		name=declaration.split("=")[0].strip()[4:];
		value=declaration.split("=")[1];
		if "[" in declaration: return syntax.format(name, convert_bracket(value.strip())[len("<item>"):-len("<item>")-1])
		else: return syntax.format(name ,parse_arg([value], ["l"]));
	else: return syntax.format(declaration[4:], "");
	
def convert_bracket(cm):
	print cm;
	locations2=[];
	start = len(cm);
	while start!=-1:
		start = cm.rfind("[",0,start);
		if start!=-1:
			end = start;
			end = cm.find("]", end+1, len(cm));
			if end-start!=1:
				cm = cm.replace(cm[start:end+1],str('<item><list>'+parse_arg(cm[start+1:end].split(","), ["item", "l"])+"</list></item>"));
			else:cm='<list></list>';
	return cm;
	
def convert_command(cmd):
	locations2=[];
	start = len(cmd);
	while start!=-1:
		start = cmd.rfind("(",0,start);
		if start!=-1:
			begin = start-1;
			while begin>-1 and cmd[begin]!="," and cmd[begin]!="(": begin-=1;
			end = start;
			end = cmd.find(")", end+1, len(cmd));
			if end-start!=1:
				if cmd[start+1]=="[": cmd = cmd[0:begin+1]+'<block s="'+cmd[begin+1:start]+'"><list>'+parse_arg(cmd[start+2:end-1].split(","), ["l"])+"</list></block>"+cmd[end+1:];	
				else: cmd = cmd[0:begin+1]+'<block s="'+cmd[begin+1:start]+'">'+parse_arg(cmd[start+1:end].split(","), ["l"])+"</block>"+cmd[end+1:];
			else:
				cmd='<block s="'+cmd[begin+1:start]+'"></block>'
	return cmd;
	
def convert_to_xml(fragment):
	temp="";
	if len(fragment.split(";"))==1:return fragment;
	for line in fragment.split(";")[:-1]:
		line = line.strip(" \n\t\r");
		if "(" in line: temp+=convert_command(line);
		elif "var " in line: temp+=convert_variable(line);
		else: temp+=line;
	return temp;

data="";	
with open(filename, "r") as raw_file:
	modules=["script", "variables"];
	data = raw_file.read();
	data="".join(data.split("\n"));
	for module in modules:
		number = data.count("<"+module+" ")+data.count("<"+module+">");
		for i in range(number):
			locations=[];
			start = len(data);
			for j in range(i+1):	
				start = data.rfind("<"+module,0,start-1);
				start = data.find(">", start, len(data));
				if start!=-1:
					end = start;
					end=data.find("</"+module+">", end+1, len(data));
					while end in locations: end=data.find("</"+module+">", end+1, len(data));
					locations.append(start);
					locations.append(end);
			#print data[start+1:end]
			#print 0;
			#print convert_to_xml(data[start+1:end])
			data = data[0:start+1]+convert_to_xml(data[start+1:end])+data[end:];
	
with open(filename+".xml", "w") as xml_file:	
	xml_file.write(data);	