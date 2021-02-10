		#Imágenes

		#Clases
	#Mago
mageIm = (" 0\n" 
	      "/█=Î\n" 
	      "/ \ ")

	#Guerrero
warriorIm = ("  0\n" 
	         "()█\ \n" 
		     " / \ ")

	#Asesino
rogueIm = (" 0\n" 
	      " █->\n" 
	      "/ \ ")

	
		#Estáticos
	#MagoVs
mageVsWarriorIm = (" 0      0 \n"
              	  "/█=Î  ()█\ \n"
	              "/ \    / \  ")

mageVsRogueIm = (" 0      0 \n"
              	  "/█=Î  <-█\n"
	              "/ \    / \  ")

mageVsMageIm = (" 0     0 \n"
              	  "/█=Î  /█=Î\n"
	              "/ \   / \  ")

	#RogueVs
rogueVsWarriorIm = ("  0      0 \n"
              	    " █->  ()█\ \n"
	                "/ \    / \  ")

rogueVsMageIm = (" 0      0    \n"
              	  " █->    █=Î \n"
	              "/ \    / \    ")

rogueVsRogueIm = (" 0      0    \n"
              	  " █->  <-█ \n"
	              "/ \    / \    ")

	#WarriorVs
warriorVsMageIm = ("  0      0   \n"
				   "()█\    /█=Î \n"	
				   " / \	/ \ ")

warriorVsRogueIm = ("  0      0   \n"
				   "()█\   <-█ \n"	
				   " / \	/ \ ")

warriorVsWarriorIm = ("  0      0   \n"
				      "()█\   ()█\  \n"	
				      " / \	/ \    ")


		#Dinámicos
	#Ataque basico Mago
mageVsWarriorBasicAIm = ("  0       0        0     0        0       0    \n"
	         	         " /█=Î   ()█\  =>   █=Î()=█   =>  /█=Î   ()█\   \n"
	   	                 " / \     / \      //    │\       / \     / \   ")

mageVsRogueBasicAIm = ("  0       0          0    0        0       0    \n"
	         	       " /█=Î   <-█\  =>     █=Î<-█   =>  /█=Î   <-█\   \n"
	   	               " / \     / \        //   │\       / \     / \   ")

mageVsMageBasicAIm = ("  0       0        0    0        0       0    \n"
	         	         " /█=Î    /█=Î   => █=ÎÎ=█   =>  /█=Î    /█=Î   \n"
	   	                 " / \     / \      //   │\       / \     / \   ")


	#Ataque básico Asesino
rogueVsMageBasicAIm = ("  0       0        0    0        0       0    \n"
	         	       "  █->   Î=█\  =>   █->Î=█   =>   █->   Î=█\   \n"
	   	               " / \     / \      //   │\       / \     / \   ")

rogueVsWarriorBasicAIm = (" 0       0        0     0        0       0    \n"
	         	         " /█->   ()█\  =>   █->()=█   =>  /█->   ()█\   \n"
	   	                 " / \     / \      //    │\       / \     / \   ")

rogueVsRogueBasicAIm = ("  0       0        0    0        0       0    \n"
	         	         " /█->   <-█\  =>   █-><-█   =>  /█->   <-█\   \n"
	   	                 " / \     / \     //    │\       / \     / \   ")



	#Ataque básico Guerrero
warriorVsMageBasicAIm = ("  0       0        0     0        0       0    \n"
	         	         "()█\    Î=█\  =>   █=()Î=█   => ()█\    Î=█\   \n"
	   	                 " / \     / \      //    │\       / \     / \   ")

warriorVsRogueBasicAIm = ("  0       0         0     0        0       0    \n"
	         	          "()█\    <-█\  =>    █=()<-█   =>  /█()   <-█\   \n"
	   	                  " / \     / \       //    │\       / \     / \   ")

warriorVsWarriorBasicAIm = ("  0       0      0      0        0       0    \n"
	         	            " /█()    /█() => █=()()=█   =>  /█()    /█()   \n"
	   	                    " / \     / \    //     │\       / \     / \   ")

frapStatic = str
frapBasic = str