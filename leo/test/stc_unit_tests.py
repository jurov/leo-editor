# -*- coding: utf-8 -*-
#@+leo-ver=5-thin
#@+node:ekr.20140527115626.17955: * @file ../test/stc_unit_tests.py
#@@first
#@+others
#@+node:ekr.20140527073639.16704: ** @testsetup
# Common setup code for all unit tests.
# **Note**: Only included for "all" and "marked" *local* runs.
trace = False
do_gc = True
    # Takes about 0.5 sec. per test.
    # Can be done at end of test.
if c.isChanged():
    c.save()
import ast
import gc
import leo.core.leoSTC as stc
import time
import imp
imp.reload(stc) # Takes about 0.003 sec.
u = stc.Utils()
u.update_run_count(verbose=True)
t2 = time.clock()
if do_gc:
    gc.collect()
if trace:
    print('@testsetup gc.collect: %s %s' % (
        (do_gc,g.timeSince(t2))))
#@+node:ekr.20140527073639.16706: ** @test DataTraverser
#@+others
#@+node:ekr.20140527125017.17956: *3* check_class_names
def check_class_names(defs_d,refs_d):
    aList = [
    'abbrevCommandsClass',
    'anchor_htmlParserClass',
    'atFile',
    'atShadowTestCase',
    'baseEditCommandsClass',
    'baseFileCommands',
    'baseLeoCompare',
    'baseLeoPlugin',
    'baseNativeTreeWidget',
    'baseTangleCommands',
    'baseTextWidget',
    'bridgeController',
    'bufferCommandsClass',
    'cScanner',
    'cSharpScanner',
    'cacher',
    'chapter',
    'chapterCommandsClass',
    'chapterController',
    'command',
    'controlCommandsClass',
    'debugCommandsClass',
    'def_node',
    'editBodyTestCase',
    'editCommandsClass',
    'editFileCommandsClass',
    'elispScanner',
    'emergencyDialog',
    'fileCommands',
    'fileLikeObject',
    'forgivingParserClass',
    'goToLineNumber',
    'helpCommandsClass',
    'htmlParserClass',
    'htmlScanner',
    'importExportTestCase',
    'iniScanner',
    'invalidPaste',
    'jEditColorizer',
    'javaScanner',
    'keyHandlerClass',
    'keyHandlerCommandsClass',
    'killBufferCommandsClass',
    'killBuffer_iter_class',
    'leoBody',
    'leoCommandsClass',
    'leoCompare',
    'leoFind',
    'leoFrame',
    'leoGui',
    'leoImportCommands',
    'leoKeyEvent',
    'leoLog',
    'leoMenu',
    'leoQLineEditWidget',
    'leoQScintillaWidget',
    'leoQTextEditWidget',
    'leoQtBaseTextWidget',
    'leoQtBody',
    'leoQtColorizer',
    'leoQtEventFilter',
    'leoQtFrame',
    'leoQtGui',
    'leoQtHeadlineWidget',
    'leoQtLog',
    'leoQtMenu',
    'leoQtMinibuffer',
    'leoQtSpellTab',
    'leoQtSyntaxHighlighter',
    'leoQtTree',
    'leoQtTreeTab',
    'leoTree',
    'leoTreeTab',
    'linkAnchorParserClass',
    'link_htmlparserClass',
    'macroCommandsClass',
    'markerClass',
    'node',
    'nodeHistory',
    'nodeIndices',
    'nullBody',
    'nullColorizer',
    'nullFrame',
    'nullGui',
    'nullIconBarClass',
    'nullLog',
    'nullMenu',
    'nullObject',
    'nullScriptingControllerClass',
    'nullStatusLineClass',
    'nullTree',
    'part_node',
    'pascalScanner',
    'phpScanner',
    'posList',
    'poslist',
    'pythonScanner',
    'qtIconBarClass',
    'qtMenuWrapper',
    'qtSearchWidget',
    'qtStatusLineClass',
    'qtTabBarWrapper',
    'queryReplaceCommandsClass',
    'readLinesClass',
    'rectangleCommandsClass',
    'recursiveImportController',
    'redirectClass',
    'registerCommandsClass',
    'root_attributes',
    'rstCommands',
    'rstScanner',
    'runTestExternallyHelperClass',
    'saxContentHandler',
    'saxNodeClass',
    'scanUtility',
    'searchCommandsClass',
    'searchWidget',
    'shadowController',
    'sourcereader',
    'sourcewriter',
    'spellCommandsClass',
    'spellTabHandler',
    'stringTextWidget',
    'tangleCommands',
    'tst_node',
    'undoer',
    'unitTestGui',
    'ust_node',
    'vimoutlinerScanner',
    'xmlScanner',
    ]
    ambiguous,undefined = [],[]
    for s in aList:
        aSet = defs_d.get(s,set())
        n = len(sorted(aSet))
        if n == 0:
            undefined.append(s)
        elif n > 1:
            ambiguous.append(s)
        s2 = pep8_class_name(s)
        aSet = defs_d.get(s2,set())
        if len(sorted(aSet)) > 1:
            g.trace('conflict',s,s2)
    g.trace('undefined...\n  %s' % '\n  '.join(sorted(undefined)))
    g.trace('ambiguous...\n  %s' % '\n  '.join(sorted(ambiguous)))
#@+node:ekr.20140527083058.16708: *3* report
def report():
    '''Report ambiguous symbols.'''
    n = 0
    for s in sorted(defs_d.keys()):
        aSet = defs_d.get(s)
        aList = sorted(aSet)
        if len(aList) > 1:
            n += 1
            # g.trace('multiple defs',s)
    return n
#@+node:ekr.20140527125017.17958: *3* pep8_class_name (remove underscores)
def pep8_class_name(s):
    '''Return the proper class name for s.'''
    assert s
    if s[0].islower():
        s = s[0].upper()+s[1:]
    return s
#@-others
project_name = 'leo'
flags = (
    'check',
    'print',
    'report',
    # 'skip',
    # 'stats',
)
files = [
    # r'c:\leo.repo\leo-editor\leo\core\leoApp.py',
    # r'c:\leo.repo\leo-editor\leo\core\leoFileCommands.py',
] or u.project_files(project_name)
if g.app.runningAllUnitTests and (len(files) > 1 or 'skip' in flags):
    self.skipTest('slow test')
# Pass 0
t = time.time()
root_d = u.p0(files,project_name,False)
p0_time = u.diff_time(t)
# DataTraverser
t = time.time()
defs_d, refs_d = {},{}
dt = stc.DataTraverser(defs_d,refs_d)
for fn in sorted(files):
    dt(fn,root_d.get(fn))
dt_time = u.diff_time(t)
if 'check' in flags:
    check_class_names(defs_d,refs_d)
if 'print' in flags:
    print('parse: %s' % p0_time)
    print('   DT: %s' % dt_time)
    print('defs: %s refs: %s: ambiguous: %s' % (
        len(sorted(defs_d.keys())),
        len(sorted(refs_d.keys())),
        report(),
    ))
    if 'stats' in flags:
        dt.print_stats()
#@-others
#@@language python
#@@tabwidth -4
#@-leo