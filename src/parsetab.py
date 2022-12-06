
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programleftTkCommaleftTkOrleftTkAndrightTkNotleftTkEqualTkNEqualleftTkLessTkLeqTkGeqTkGreaterleftTkPlusTkMinusleftTkMultrightUMinusTkAnd TkArray TkArrow TkAsig TkBool TkCBlock TkCBracket TkClosePar TkComma TkComment TkConcat TkDeclare TkDo TkEqual TkFalse TkFi TkFor TkGeq TkGreater TkGuard TkId TkIf TkIn TkInt TkLeq TkLess TkMinus TkMult TkNEqual TkNewLine TkNot TkNum TkOBlock TkOBracket TkOd TkOpenPar TkOr TkPlus TkPrint TkRof TkSemicolon TkSkip TkSoForth TkSpace TkString TkTo TkTrue TkTwoPoints\n                program : instBlock \n            \n            instBlock : TkOBlock declare TkCBlock\n                      | TkOBlock declare code TkCBlock\n                      | TkOBlock code TkCBlock\n            \n                declare : TkDeclare declaration\n                        | TkDeclare seqDeclare\n            \n                declaration : DeclaList TkTwoPoints type\n            \n            DeclaList : TkId TkComma DeclaList\n                        | TkId\n            \n                seqDeclare : declaration TkSemicolon declaration\n                           | seqDeclare TkSemicolon declaration\n            \n                type : TkInt\n                     | TkBool\n                     | TkArray TkOBracket TkNum TkSoForth TkNum TkCBracket\n                     | TkArray TkOBracket TkMinus TkNum TkSoForth TkMinus TkNum TkCBracket\n                     | TkArray TkOBracket TkNum TkSoForth TkMinus TkNum TkCBracket\n                     | TkArray TkOBracket TkMinus TkNum TkSoForth TkNum TkCBracket\n            \n                code : instruction\n                     | sequencing\n            \n                sequencing : instruction TkSemicolon instruction\n                           | sequencing TkSemicolon instruction\n            \n                instPrint : TkPrint printAble\n                          | TkPrint instConcat\n            \n                instSkip : TkSkip\n            \n                instConcat : printAble TkConcat  printAble\n                           | instConcat TkConcat printAble\n            \n            printAble : TkString\n            \n            printAble : exp\n            \n                arrayIni : exp TkComma exp\n            \n                arrayIni : arrayIni TkComma exp \n            \n                instAsig : TkId TkAsig arrayIni\n                         | TkId TkAsig exp \n                         | TkId TkAsig modArray\n            \n                instruction : instPrint\n                            | instAsig\n                            | instSkip\n                            | instBlock\n                            | instFor\n                            | instIf\n                            | instDo\n            \n                consArray : TkId TkOBracket exp TkCBracket\n            \n                consArray : modArray TkOBracket exp TkCBracket\n            \n                modArray : modArray TkOpenPar exp TkTwoPoints exp TkClosePar\n                         | finish\n                \n            \n                finish : TkId TkOpenPar exp TkTwoPoints exp TkClosePar\n            \n                exp : exp TkPlus exp\n                    | exp TkMinus exp\n                    | exp TkMult exp\n            \n                exp : exp TkAnd exp\n                    | exp TkOr exp\n            \n                exp : exp TkLess exp\n                    | exp TkLeq exp\n                    | exp TkGeq exp\n                    | exp TkGreater exp\n            \n                exp : exp TkEqual exp\n                    | exp TkNEqual exp\n            \n                exp : TkNot exp\n                    | TkOpenPar exp TkClosePar\n                    | consArray\n            \n                exp : TkMinus exp %prec UMinus\n            \n                exp : TkNum\n            \n                exp : TkTrue\n                    | TkFalse\n            \n                exp : TkId \n            \n                instFor : TkFor TkId TkIn exp TkTo exp TkArrow code TkRof\n            \n                instIf : TkIf guards TkFi\n            \n                instDo : TkDo guards TkOd\n            \n                guards : guards TkGuard then \n                       | then\n            \n                then : exp TkArrow code\n            \n            ignorados : TkComment\n                      | TkSpace\n                      | TkNewLine\n                      | ignorados\n            '
    
_lr_action_items = {'TkOBlock':([0,3,4,25,26,29,30,84,86,87,88,89,90,133,138,143,145,146,],[3,3,3,-5,-6,3,3,3,-10,-11,-7,-12,-13,3,-14,-16,-17,-15,]),'$end':([1,2,22,24,51,],[0,-1,-2,-4,-3,]),'TkDeclare':([3,],[6,]),'TkPrint':([3,4,25,26,29,30,84,86,87,88,89,90,133,138,143,145,146,],[16,16,-5,-6,16,16,16,-10,-11,-7,-12,-13,16,-14,-16,-17,-15,]),'TkId':([3,4,6,16,19,20,21,25,26,29,30,35,36,37,45,52,53,55,58,59,60,61,62,63,64,65,66,67,68,69,70,74,75,76,77,81,83,84,86,87,88,89,90,111,112,118,120,123,133,138,143,145,146,],[17,17,28,42,46,42,42,-5,-6,17,17,42,42,42,42,28,28,28,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,17,-10,-11,-7,-12,-13,42,42,42,42,42,17,-14,-16,-17,-15,]),'TkSkip':([3,4,25,26,29,30,84,86,87,88,89,90,133,138,143,145,146,],[18,18,-5,-6,18,18,18,-10,-11,-7,-12,-13,18,-14,-16,-17,-15,]),'TkFor':([3,4,25,26,29,30,84,86,87,88,89,90,133,138,143,145,146,],[19,19,-5,-6,19,19,19,-10,-11,-7,-12,-13,19,-14,-16,-17,-15,]),'TkIf':([3,4,25,26,29,30,84,86,87,88,89,90,133,138,143,145,146,],[20,20,-5,-6,20,20,20,-10,-11,-7,-12,-13,20,-14,-16,-17,-15,]),'TkDo':([3,4,25,26,29,30,84,86,87,88,89,90,133,138,143,145,146,],[21,21,-5,-6,21,21,21,-10,-11,-7,-12,-13,21,-14,-16,-17,-15,]),'TkCBlock':([4,5,7,8,9,10,11,12,13,14,15,18,22,23,24,25,26,31,32,33,34,38,39,40,41,42,44,51,56,57,71,72,78,79,80,82,85,86,87,88,89,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,117,119,121,122,131,132,138,142,143,145,146,],[22,24,-18,-19,-34,-35,-36,-37,-38,-39,-40,-24,-2,51,-4,-5,-6,-22,-23,-27,-28,-59,-61,-62,-63,-64,-44,-3,-20,-21,-60,-57,-31,-32,-33,-66,-67,-10,-11,-7,-12,-13,-25,-26,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-58,-41,-42,-30,-29,-45,-43,-14,-65,-16,-17,-15,]),'TkFi':([7,8,9,10,11,12,13,14,15,18,22,24,31,32,33,34,38,39,40,41,42,44,47,48,51,56,57,71,72,78,79,80,82,85,93,94,95,96,97,98,99,100,101,102,103,104,105,106,114,115,117,119,121,122,131,132,142,],[-18,-19,-34,-35,-36,-37,-38,-39,-40,-24,-2,-4,-22,-23,-27,-28,-59,-61,-62,-63,-64,-44,82,-69,-3,-20,-21,-60,-57,-31,-32,-33,-66,-67,-25,-26,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-58,-68,-70,-41,-42,-30,-29,-45,-43,-65,]),'TkGuard':([7,8,9,10,11,12,13,14,15,18,22,24,31,32,33,34,38,39,40,41,42,44,47,48,50,51,56,57,71,72,78,79,80,82,85,93,94,95,96,97,98,99,100,101,102,103,104,105,106,114,115,117,119,121,122,131,132,142,],[-18,-19,-34,-35,-36,-37,-38,-39,-40,-24,-2,-4,-22,-23,-27,-28,-59,-61,-62,-63,-64,-44,83,-69,83,-3,-20,-21,-60,-57,-31,-32,-33,-66,-67,-25,-26,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-58,-68,-70,-41,-42,-30,-29,-45,-43,-65,]),'TkOd':([7,8,9,10,11,12,13,14,15,18,22,24,31,32,33,34,38,39,40,41,42,44,48,50,51,56,57,71,72,78,79,80,82,85,93,94,95,96,97,98,99,100,101,102,103,104,105,106,114,115,117,119,121,122,131,132,142,],[-18,-19,-34,-35,-36,-37,-38,-39,-40,-24,-2,-4,-22,-23,-27,-28,-59,-61,-62,-63,-64,-44,-69,85,-3,-20,-21,-60,-57,-31,-32,-33,-66,-67,-25,-26,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-58,-68,-70,-41,-42,-30,-29,-45,-43,-65,]),'TkRof':([7,8,9,10,11,12,13,14,15,18,22,24,31,32,33,34,38,39,40,41,42,44,51,56,57,71,72,78,79,80,82,85,93,94,95,96,97,98,99,100,101,102,103,104,105,106,117,119,121,122,131,132,137,142,],[-18,-19,-34,-35,-36,-37,-38,-39,-40,-24,-2,-4,-22,-23,-27,-28,-59,-61,-62,-63,-64,-44,-3,-20,-21,-60,-57,-31,-32,-33,-66,-67,-25,-26,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-58,-41,-42,-30,-29,-45,-43,142,-65,]),'TkSemicolon':([7,8,9,10,11,12,13,14,15,18,22,24,25,26,31,32,33,34,38,39,40,41,42,44,51,56,57,71,72,78,79,80,82,85,86,87,88,89,90,93,94,95,96,97,98,99,100,101,102,103,104,105,106,117,119,121,122,131,132,138,142,143,145,146,],[29,30,-34,-35,-36,-37,-38,-39,-40,-24,-2,-4,52,53,-22,-23,-27,-28,-59,-61,-62,-63,-64,-44,-3,-20,-21,-60,-57,-31,-32,-33,-66,-67,-10,-11,-7,-12,-13,-25,-26,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-58,-41,-42,-30,-29,-45,-43,-14,-65,-16,-17,-15,]),'TkString':([16,58,59,],[33,33,33,]),'TkNot':([16,20,21,35,36,37,45,58,59,60,61,62,63,64,65,66,67,68,69,70,74,75,76,77,81,83,111,112,118,120,123,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'TkOpenPar':([16,20,21,35,36,37,42,43,44,45,58,59,60,61,62,63,64,65,66,67,68,69,70,74,75,76,77,80,81,83,111,112,118,120,123,131,132,],[37,37,37,37,37,37,75,77,-44,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,77,37,37,37,37,37,37,37,-45,-43,]),'TkMinus':([16,20,21,34,35,36,37,38,39,40,41,42,45,49,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,81,83,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,117,118,119,120,121,122,123,126,127,128,129,136,],[35,35,35,61,35,35,35,-59,-61,-62,-63,-64,35,61,35,35,35,35,35,35,35,35,35,35,35,35,35,-60,61,61,35,35,35,35,61,35,35,-46,-47,-48,61,61,61,61,61,61,61,61,-58,61,61,61,61,35,35,61,125,-41,35,-42,35,61,61,35,61,61,61,135,140,]),'TkNum':([16,20,21,35,36,37,45,58,59,60,61,62,63,64,65,66,67,68,69,70,74,75,76,77,81,83,111,112,116,118,120,123,125,129,135,136,140,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,124,39,39,39,130,134,139,141,144,]),'TkTrue':([16,20,21,35,36,37,45,58,59,60,61,62,63,64,65,66,67,68,69,70,74,75,76,77,81,83,111,112,118,120,123,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'TkFalse':([16,20,21,35,36,37,45,58,59,60,61,62,63,64,65,66,67,68,69,70,74,75,76,77,81,83,111,112,118,120,123,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'TkAsig':([17,],[45,]),'TkTwoPoints':([27,28,38,39,40,41,42,71,72,92,95,96,97,98,99,100,101,102,103,104,105,106,108,110,117,119,],[54,-9,-59,-61,-62,-63,-64,-60,-57,-8,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-58,118,120,-41,-42,]),'TkComma':([28,38,39,40,41,42,71,72,78,79,95,96,97,98,99,100,101,102,103,104,105,106,117,119,121,122,],[55,-59,-61,-62,-63,-64,-60,-57,111,112,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-58,-41,-42,-30,-29,]),'TkConcat':([31,32,33,34,38,39,40,41,42,71,72,93,94,95,96,97,98,99,100,101,102,103,104,105,106,117,119,],[58,59,-27,-28,-59,-61,-62,-63,-64,-60,-57,-25,-26,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-58,-41,-42,]),'TkPlus':([34,38,39,40,41,42,49,71,72,73,79,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,113,117,119,121,122,126,127,128,],[60,-59,-61,-62,-63,-64,60,-60,60,60,60,-46,-47,-48,60,60,60,60,60,60,60,60,-58,60,60,60,60,60,-41,-42,60,60,60,60,60,]),'TkMult':([34,38,39,40,41,42,49,71,72,73,79,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,113,117,119,121,122,126,127,128,],[62,-59,-61,-62,-63,-64,62,-60,62,62,62,62,62,-48,62,62,62,62,62,62,62,62,-58,62,62,62,62,62,-41,-42,62,62,62,62,62,]),'TkAnd':([34,38,39,40,41,42,49,71,72,73,79,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,113,117,119,121,122,126,127,128,],[63,-59,-61,-62,-63,-64,63,-60,-57,63,63,-46,-47,-48,-49,63,-51,-52,-53,-54,-55,-56,-58,63,63,63,63,63,-41,-42,63,63,63,63,63,]),'TkOr':([34,38,39,40,41,42,49,71,72,73,79,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,113,117,119,121,122,126,127,128,],[64,-59,-61,-62,-63,-64,64,-60,-57,64,64,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-58,64,64,64,64,64,-41,-42,64,64,64,64,64,]),'TkLess':([34,38,39,40,41,42,49,71,72,73,79,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,113,117,119,121,122,126,127,128,],[65,-59,-61,-62,-63,-64,65,-60,65,65,65,-46,-47,-48,65,65,-51,-52,-53,-54,65,65,-58,65,65,65,65,65,-41,-42,65,65,65,65,65,]),'TkLeq':([34,38,39,40,41,42,49,71,72,73,79,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,113,117,119,121,122,126,127,128,],[66,-59,-61,-62,-63,-64,66,-60,66,66,66,-46,-47,-48,66,66,-51,-52,-53,-54,66,66,-58,66,66,66,66,66,-41,-42,66,66,66,66,66,]),'TkGeq':([34,38,39,40,41,42,49,71,72,73,79,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,113,117,119,121,122,126,127,128,],[67,-59,-61,-62,-63,-64,67,-60,67,67,67,-46,-47,-48,67,67,-51,-52,-53,-54,67,67,-58,67,67,67,67,67,-41,-42,67,67,67,67,67,]),'TkGreater':([34,38,39,40,41,42,49,71,72,73,79,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,113,117,119,121,122,126,127,128,],[68,-59,-61,-62,-63,-64,68,-60,68,68,68,-46,-47,-48,68,68,-51,-52,-53,-54,68,68,-58,68,68,68,68,68,-41,-42,68,68,68,68,68,]),'TkEqual':([34,38,39,40,41,42,49,71,72,73,79,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,113,117,119,121,122,126,127,128,],[69,-59,-61,-62,-63,-64,69,-60,69,69,69,-46,-47,-48,69,69,-51,-52,-53,-54,-55,-56,-58,69,69,69,69,69,-41,-42,69,69,69,69,69,]),'TkNEqual':([34,38,39,40,41,42,49,71,72,73,79,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,113,117,119,121,122,126,127,128,],[70,-59,-61,-62,-63,-64,70,-60,70,70,70,-46,-47,-48,70,70,-51,-52,-53,-54,-55,-56,-58,70,70,70,70,70,-41,-42,70,70,70,70,70,]),'TkArrow':([38,39,40,41,42,49,71,72,95,96,97,98,99,100,101,102,103,104,105,106,117,119,128,],[-59,-61,-62,-63,-64,84,-60,-57,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-58,-41,-42,133,]),'TkClosePar':([38,39,40,41,42,71,72,73,95,96,97,98,99,100,101,102,103,104,105,106,117,119,126,127,],[-59,-61,-62,-63,-64,-60,-57,106,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-58,-41,-42,131,132,]),'TkCBracket':([38,39,40,41,42,71,72,95,96,97,98,99,100,101,102,103,104,105,106,107,109,117,119,134,139,141,144,],[-59,-61,-62,-63,-64,-60,-57,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-58,117,119,-41,-42,138,143,145,146,]),'TkTo':([38,39,40,41,42,71,72,95,96,97,98,99,100,101,102,103,104,105,106,113,117,119,],[-59,-61,-62,-63,-64,-60,-57,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-58,123,-41,-42,]),'TkOBracket':([42,43,44,80,91,131,132,],[74,76,-44,76,116,-45,-43,]),'TkIn':([46,],[81,]),'TkInt':([54,],[89,]),'TkBool':([54,],[90,]),'TkArray':([54,],[91,]),'TkSoForth':([124,130,],[129,136,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instBlock':([0,3,4,29,30,84,133,],[2,12,12,12,12,12,12,]),'declare':([3,],[4,]),'code':([3,4,84,133,],[5,23,115,137,]),'instruction':([3,4,29,30,84,133,],[7,7,56,57,7,7,]),'sequencing':([3,4,84,133,],[8,8,8,8,]),'instPrint':([3,4,29,30,84,133,],[9,9,9,9,9,9,]),'instAsig':([3,4,29,30,84,133,],[10,10,10,10,10,10,]),'instSkip':([3,4,29,30,84,133,],[11,11,11,11,11,11,]),'instFor':([3,4,29,30,84,133,],[13,13,13,13,13,13,]),'instIf':([3,4,29,30,84,133,],[14,14,14,14,14,14,]),'instDo':([3,4,29,30,84,133,],[15,15,15,15,15,15,]),'declaration':([6,52,53,],[25,86,87,]),'seqDeclare':([6,],[26,]),'DeclaList':([6,52,53,55,],[27,27,27,92,]),'printAble':([16,58,59,],[31,93,94,]),'instConcat':([16,],[32,]),'exp':([16,20,21,35,36,37,45,58,59,60,61,62,63,64,65,66,67,68,69,70,74,75,76,77,81,83,111,112,118,120,123,],[34,49,49,71,72,73,79,34,34,95,96,97,98,99,100,101,102,103,104,105,107,108,109,110,113,49,121,122,126,127,128,]),'consArray':([16,20,21,35,36,37,45,58,59,60,61,62,63,64,65,66,67,68,69,70,74,75,76,77,81,83,111,112,118,120,123,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'modArray':([16,20,21,35,36,37,45,58,59,60,61,62,63,64,65,66,67,68,69,70,74,75,76,77,81,83,111,112,118,120,123,],[43,43,43,43,43,43,80,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'finish':([16,20,21,35,36,37,45,58,59,60,61,62,63,64,65,66,67,68,69,70,74,75,76,77,81,83,111,112,118,120,123,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'guards':([20,21,],[47,50,]),'then':([20,21,83,],[48,48,114,]),'arrayIni':([45,],[78,]),'type':([54,],[88,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instBlock','program',1,'p_program','AnalizadorSintactico.py',45),
  ('instBlock -> TkOBlock declare TkCBlock','instBlock',3,'p_instBlock','AnalizadorSintactico.py',54),
  ('instBlock -> TkOBlock declare code TkCBlock','instBlock',4,'p_instBlock','AnalizadorSintactico.py',55),
  ('instBlock -> TkOBlock code TkCBlock','instBlock',3,'p_instBlock','AnalizadorSintactico.py',56),
  ('declare -> TkDeclare declaration','declare',2,'p_declare','AnalizadorSintactico.py',76),
  ('declare -> TkDeclare seqDeclare','declare',2,'p_declare','AnalizadorSintactico.py',77),
  ('declaration -> DeclaList TkTwoPoints type','declaration',3,'p_declaration','AnalizadorSintactico.py',93),
  ('DeclaList -> TkId TkComma DeclaList','DeclaList',3,'p_decaList','AnalizadorSintactico.py',110),
  ('DeclaList -> TkId','DeclaList',1,'p_decaList','AnalizadorSintactico.py',111),
  ('seqDeclare -> declaration TkSemicolon declaration','seqDeclare',3,'p_seqDeclare','AnalizadorSintactico.py',121),
  ('seqDeclare -> seqDeclare TkSemicolon declaration','seqDeclare',3,'p_seqDeclare','AnalizadorSintactico.py',122),
  ('type -> TkInt','type',1,'p_type','AnalizadorSintactico.py',138),
  ('type -> TkBool','type',1,'p_type','AnalizadorSintactico.py',139),
  ('type -> TkArray TkOBracket TkNum TkSoForth TkNum TkCBracket','type',6,'p_type','AnalizadorSintactico.py',140),
  ('type -> TkArray TkOBracket TkMinus TkNum TkSoForth TkMinus TkNum TkCBracket','type',8,'p_type','AnalizadorSintactico.py',141),
  ('type -> TkArray TkOBracket TkNum TkSoForth TkMinus TkNum TkCBracket','type',7,'p_type','AnalizadorSintactico.py',142),
  ('type -> TkArray TkOBracket TkMinus TkNum TkSoForth TkNum TkCBracket','type',7,'p_type','AnalizadorSintactico.py',143),
  ('code -> instruction','code',1,'p_code','AnalizadorSintactico.py',172),
  ('code -> sequencing','code',1,'p_code','AnalizadorSintactico.py',173),
  ('sequencing -> instruction TkSemicolon instruction','sequencing',3,'p_sequencing','AnalizadorSintactico.py',180),
  ('sequencing -> sequencing TkSemicolon instruction','sequencing',3,'p_sequencing','AnalizadorSintactico.py',181),
  ('instPrint -> TkPrint printAble','instPrint',2,'p_instPrint','AnalizadorSintactico.py',192),
  ('instPrint -> TkPrint instConcat','instPrint',2,'p_instPrint','AnalizadorSintactico.py',193),
  ('instSkip -> TkSkip','instSkip',1,'p_instSkip','AnalizadorSintactico.py',201),
  ('instConcat -> printAble TkConcat printAble','instConcat',3,'p_instConcat','AnalizadorSintactico.py',209),
  ('instConcat -> instConcat TkConcat printAble','instConcat',3,'p_instConcat','AnalizadorSintactico.py',210),
  ('printAble -> TkString','printAble',1,'p_printeAble1','AnalizadorSintactico.py',217),
  ('printAble -> exp','printAble',1,'p_printeAble2','AnalizadorSintactico.py',224),
  ('arrayIni -> exp TkComma exp','arrayIni',3,'p_arrayIni','AnalizadorSintactico.py',231),
  ('arrayIni -> arrayIni TkComma exp','arrayIni',3,'p_arrayIni2','AnalizadorSintactico.py',239),
  ('instAsig -> TkId TkAsig arrayIni','instAsig',3,'p_instAsig','AnalizadorSintactico.py',247),
  ('instAsig -> TkId TkAsig exp','instAsig',3,'p_instAsig','AnalizadorSintactico.py',248),
  ('instAsig -> TkId TkAsig modArray','instAsig',3,'p_instAsig','AnalizadorSintactico.py',249),
  ('instruction -> instPrint','instruction',1,'p_instruction','AnalizadorSintactico.py',269),
  ('instruction -> instAsig','instruction',1,'p_instruction','AnalizadorSintactico.py',270),
  ('instruction -> instSkip','instruction',1,'p_instruction','AnalizadorSintactico.py',271),
  ('instruction -> instBlock','instruction',1,'p_instruction','AnalizadorSintactico.py',272),
  ('instruction -> instFor','instruction',1,'p_instruction','AnalizadorSintactico.py',273),
  ('instruction -> instIf','instruction',1,'p_instruction','AnalizadorSintactico.py',274),
  ('instruction -> instDo','instruction',1,'p_instruction','AnalizadorSintactico.py',275),
  ('consArray -> TkId TkOBracket exp TkCBracket','consArray',4,'p_consArray','AnalizadorSintactico.py',282),
  ('consArray -> modArray TkOBracket exp TkCBracket','consArray',4,'p_consArray1','AnalizadorSintactico.py',288),
  ('modArray -> modArray TkOpenPar exp TkTwoPoints exp TkClosePar','modArray',6,'p_modArray','AnalizadorSintactico.py',294),
  ('modArray -> finish','modArray',1,'p_modArray','AnalizadorSintactico.py',295),
  ('finish -> TkId TkOpenPar exp TkTwoPoints exp TkClosePar','finish',6,'p_modArray1','AnalizadorSintactico.py',305),
  ('exp -> exp TkPlus exp','exp',3,'p_opBin','AnalizadorSintactico.py',312),
  ('exp -> exp TkMinus exp','exp',3,'p_opBin','AnalizadorSintactico.py',313),
  ('exp -> exp TkMult exp','exp',3,'p_opBin','AnalizadorSintactico.py',314),
  ('exp -> exp TkAnd exp','exp',3,'p_opBin2','AnalizadorSintactico.py',330),
  ('exp -> exp TkOr exp','exp',3,'p_opBin2','AnalizadorSintactico.py',331),
  ('exp -> exp TkLess exp','exp',3,'p_opBin3','AnalizadorSintactico.py',344),
  ('exp -> exp TkLeq exp','exp',3,'p_opBin3','AnalizadorSintactico.py',345),
  ('exp -> exp TkGeq exp','exp',3,'p_opBin3','AnalizadorSintactico.py',346),
  ('exp -> exp TkGreater exp','exp',3,'p_opBin3','AnalizadorSintactico.py',347),
  ('exp -> exp TkEqual exp','exp',3,'p_opBin4','AnalizadorSintactico.py',366),
  ('exp -> exp TkNEqual exp','exp',3,'p_opBin4','AnalizadorSintactico.py',367),
  ('exp -> TkNot exp','exp',2,'p_exp','AnalizadorSintactico.py',382),
  ('exp -> TkOpenPar exp TkClosePar','exp',3,'p_exp','AnalizadorSintactico.py',383),
  ('exp -> consArray','exp',1,'p_exp','AnalizadorSintactico.py',384),
  ('exp -> TkMinus exp','exp',2,'p_literales','AnalizadorSintactico.py',400),
  ('exp -> TkNum','exp',1,'p_literales1','AnalizadorSintactico.py',410),
  ('exp -> TkTrue','exp',1,'p_literales2','AnalizadorSintactico.py',417),
  ('exp -> TkFalse','exp',1,'p_literales2','AnalizadorSintactico.py',418),
  ('exp -> TkId','exp',1,'p_id','AnalizadorSintactico.py',426),
  ('instFor -> TkFor TkId TkIn exp TkTo exp TkArrow code TkRof','instFor',9,'p_instFor','AnalizadorSintactico.py',440),
  ('instIf -> TkIf guards TkFi','instIf',3,'p_instIf','AnalizadorSintactico.py',447),
  ('instDo -> TkDo guards TkOd','instDo',3,'p_instDo','AnalizadorSintactico.py',454),
  ('guards -> guards TkGuard then','guards',3,'p_guards','AnalizadorSintactico.py',461),
  ('guards -> then','guards',1,'p_guards','AnalizadorSintactico.py',462),
  ('then -> exp TkArrow code','then',3,'p_then','AnalizadorSintactico.py',472),
  ('ignorados -> TkComment','ignorados',1,'p_ignorados','AnalizadorSintactico.py',478),
  ('ignorados -> TkSpace','ignorados',1,'p_ignorados','AnalizadorSintactico.py',479),
  ('ignorados -> TkNewLine','ignorados',1,'p_ignorados','AnalizadorSintactico.py',480),
  ('ignorados -> ignorados','ignorados',1,'p_ignorados','AnalizadorSintactico.py',481),
]
