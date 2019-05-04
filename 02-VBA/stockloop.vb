Sub stockloop()

    Dim ws As Worksheet

    For Each ws In Worksheets
        
        ws.Activate
        
        Dim ticker As String
        Dim volume As Double
        Dim yearchange As Double
        Dim percentchange As Double
        Dim lastclose As Double
        Dim firstopen As Double
        Dim row As Double
        Dim column As Double
        
        
        Range("I1").Value = "Ticker"
        Range("J1").Value = "Yearly Change"
        Range("K1").Value = "Percent Change"
        Range("L1").Value = "Total Stock Volume"
		Range("O2").Value = "Greatest % Increase"
        Range("O3").Value = "Greatest % Decrease"
        Range("O4").Value = "Greatest Total Volume"
        Range("P1").Value = "Ticker"
		Range("Q1").Value = "Value"
 
        volume = 0
        yearchange = 0
        percentchange = 0
        lastclose = 0
        firstopen = 0
        row = 2
        column = 1
        
        lastrow = Cells(Rows.Count, 1).End(xlUp).row
        
        firstopen = Cells(2, column + 2).Value

        For i = 2 To lastrow
            
            If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
                
                ticker = Cells(i, 1).Value
                
                Range("I" & row).Value = ticker

                lastclose = Cells(i, 6).Value
                
                yearchange = lastclose - firstopen
                
                Range("J" & row).Value = yearchange
            
                volume = volume + Cells(i, 7).Value
                
                Range("L" & row).Value = volume
                
                If (firstopen = 0 And lastclose = 0) Then
                    
                    percentchange = 0
                    
                ElseIf (firstopen = 0 And lastclose <> 0) Then
                
                    percentchange = 1
                    
                Else
                    percentchange = yearchange / firstopen
                    
                    Range("K" & row).Value = Percent_Change
                    
                    Range("K" & row).NumberFormat = "0.00%"
                
                End If
                
                Range("K" & row).Value = percentchange
                
                Range("K" & row).NumberFormat = "0.00%"
                
                row = row + 1
                
                firstopen = Cells(i + 1, column + 2)
                
                volume = 0
            Else
                
                volume = volume + Cells(i, column + 6).Value

            End If
            
        Next i
        
        lastrow2 = Cells(Rows.Count, 9).End(xlUp).row
        
        For j = 2 To lastrow2
        
            If (Cells(j, 10).Value > 0 Or Cells(j, 10).Value = 0) Then
			
                Cells(j, 10).Interior.ColorIndex = 10
				
            ElseIf Cells(j, 10).Value < 0 Then
			
                Cells(j, 10).Interior.ColorIndex = 3
				
			End If
			
        Next j
		
		For z = 2 To lastrow2
		
		If Cells(z, 11).Value = Application.WorksheetFunction.Max(WS.Range("K2:K" & lastrow2)) Then
		
                Cells(2, 16).Value = Cells(z, 9).Value
                Cells(2, 17).Value = Cells(z, 11).Value
                Cells(2, 17).NumberFormat = "0.00%"
				
            ElseIf Cells(Z, 11).Value = Application.WorksheetFunction.Min(WS.Range("K2:K" & lastrow2)) Then
			
                Cells(3, 16).Value = Cells(z, 9).Value
                Cells(3, 17).Value = Cells(z, 11).Value
                Cells(3, 17).NumberFormat = "0.00%"
				
            ElseIf Cells(z, Column + 11).Value = Application.WorksheetFunction.Max(WS.Range("L2:L" & lastrow2)) Then
			
                Cells(4, 16).Value = Cells(z, 9).Value
                Cells(4, 17).Value = Cells(z, 12).Value
				
            End If
			
		Next Z
			
    
    Next ws
 
End Sub