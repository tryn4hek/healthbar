
class onHealthBar:
    
    def HealthBarStyle(totlH,maxh,packStyle,minPackStyle):
        healthParameter = 10
        totalHealth = totlH
        maxHealth = maxh
        
        packPerHealth = maxHealth / 10
        
        HealthPackStyle = packStyle
        HealthBarStyle = "[{}{}]"
        
        if totalHealth >= packPerHealth*9 and totalHealth < maxh:
            onHealthParameter = healthParameter - 1
            return HealthBarStyle.format(HealthPackStyle*onHealthParameter,minPackStyle*1)
            
        elif totalHealth >= packPerHealth*8 and totalHealth < packPerHealth*9:
            onHealthParameter = healthParameter -2
            return HealthBarStyle.format(HealthPackStyle*onHealthParameter,minPackStyle*2)
            
        elif totalHealth >= packPerHealth*7 and totalHealth < packPerHealth*8:
            onHealthParameter = healthParameter -3
            return HealthBarStyle.format(HealthPackStyle*onHealthParameter,minPackStyle*3)
            
        elif totalHealth >= packPerHealth*6 and totalHealth < packPerHealth*7:
            onHealthParameter = healthParameter -4
            return HealthBarStyle.format(HealthPackStyle*onHealthParameter,minPackStyle*4)
            
        elif totalHealth >= packPerHealth*5 and totalHealth < packPerHealth*6:
            onHealthParameter = healthParameter -5
            return HealthBarStyle.format(HealthPackStyle*onHealthParameter,minPackStyle*5)
            
        elif totalHealth >= packPerHealth*4 and totalHealth < packPerHealth*5:
            onHealthParameter = healthParameter -6
            return HealthBarStyle.format(HealthPackStyle*onHealthParameter,minPackStyle*6)
            
        elif totalHealth >= packPerHealth*3 and totalHealth < packPerHealth*4:
            onHealthParameter = healthParameter -7
            return HealthBarStyle.format(HealthPackStyle*onHealthParameter,minPackStyle*7)
            
        elif totalHealth >= packPerHealth*2 and totalHealth < packPerHealth*3:
            onHealthParameter = healthParameter -8
            return HealthBarStyle.format(HealthPackStyle*onHealthParameter,minPackStyle*8)
            
        elif totalHealth >= packPerHealth*1 and totalHealth < packPerHealth*2:
            onHealthParameter = healthParameter -9
            return HealthBarStyle.format(HealthPackStyle*onHealthParameter,minPackStyle*9)
            
        else:
            return HealthBarStyle.format(HealthPackStyle*healthParameter,"")

