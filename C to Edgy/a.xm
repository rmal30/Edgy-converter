<project name="a.xml" app="Snap! 4.0, http://snap.berkeley.edu" version="1" uuid="d49433b0-ddbc-11e4-8037-db7ae9465080">
<stage name="Stage" width="480" height="360" costume="0" tempo="60" threadsafe="false" lines="round" codify="false" scheduled="false" id="1">
<variables></variables><blocks></blocks><scripts></scripts>
<sprites>
<sprite name="Graph" idx="1" x="0" y="0" heading="90" scale="1" rotation="1" draggable="false" costume="0" color="80,80,80" pen="tip" id="8">
<costumes><list id="9"></list></costumes> <sounds><list id="10"></list></sounds>
<variables></variables>
<blocks></blocks>
<scripts>
		<script>
			receiveGo(); 
			doSetVar('a','0');
			doChangeVar('a','1');
			doSetVar('a',reportNewList(['1','2']));
			doSayFor(reportListItem('1',*a),'2');
			doAddToList('thing', *a);
			doDeleteFromList('1',*a);
			doConcatToList(reportNewList(['1']), *a);
			doIfElse(
reportNot(reportEquals(reportSum('2','1'),'3')),<script>doWait('1');</script>,<script>doPauseAll();</script>);
			doNumericFor('i', '1', '10',<script>doPauseAll();</script>);
</script>
</scripts>
<graph> {&quot;directed&quot;:false,&quot;multigraph&quot;:false,&quot;graph&quot;:[[&quot;__costumes__&quot;,{}]],&quot;nodes&quot;:[],&quot;links&quot;:[]}</graph><nodeattrs></nodeattrs><edgeattrs></edgeattrs></sprite><watcher var="a" style="normal" x="92" y="43" color="243,118,29" extX="80" extY="70"/></sprites><nodeattrs></nodeattrs><edgeattrs></edgeattrs></stage><hidden></hidden><headers></headers><code></code><blocks></blocks><variables>
var a = [[['0','1'],['2','3']],['4','5']];
</variables></project>
			