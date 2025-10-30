package com.example.basiccalculator;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    TextView number;
    double num1 = 0, num2 = 0;
    String op = "";
    Button bt0, bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9, add, sub, mul, div, deci, equal, clear;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        number = findViewById(R.id.etnum);
        //Numbers
        bt0 = findViewById(R.id.b0);
        bt1 = findViewById(R.id.b1);
        bt2 = findViewById(R.id.b2);
        bt3 = findViewById(R.id.b3);
        bt4 = findViewById(R.id.b4);
        bt5 = findViewById(R.id.b5);
        bt6 = findViewById(R.id.b6);
        bt7 = findViewById(R.id.b7);
        bt8 = findViewById(R.id.b8);
        bt9 = findViewById(R.id.b9);
        //Operators
        add = findViewById(R.id.add);
        sub = findViewById(R.id.sub);
        mul = findViewById(R.id.mul);
        div = findViewById(R.id.div);
        deci = findViewById(R.id.deci);
        equal = findViewById(R.id.equal);
        clear = findViewById(R.id.delete);
        //Set click listeners
        bt0.setOnClickListener(this);
        bt1.setOnClickListener(this);
        bt2.setOnClickListener(this);
        bt3.setOnClickListener(this);
        bt4.setOnClickListener(this);
        bt5.setOnClickListener(this);
        bt6.setOnClickListener(this);
        bt7.setOnClickListener(this);
        bt8.setOnClickListener(this);
        bt9.setOnClickListener(this);
        add.setOnClickListener(this);
        sub.setOnClickListener(this);
        mul.setOnClickListener(this);
        div.setOnClickListener(this);
        deci.setOnClickListener(this);
        equal.setOnClickListener(this);
        clear.setOnClickListener(this);
    }
    @Override
    public void onClick(View view) {
        Button b = (Button) view;
        if (view == clear)
        {
            number.setText("");
        }
        else if (view == sub || view == add || view == mul || view == div)
        {
            num1 = Integer.parseInt(number.getText().toString());
            op = b.getText().toString();
            number.setText("");
        }
        else if (view == equal)
        {
            num2 = Integer.parseInt(number.getText().toString());
            if (op.equals("+"))
            {
                number.setText(num1 + num2 + "");
            }
            else if (op.equals("-"))
            {
                number.setText(num1 - num2 + "");
            }
            else if (op.equals("*"))
            {
                number.setText(num1 * num2 + "");
            }
            else if(op.equals("/"))
            {
                number.setText(num1 / num2 + "");
            }
        }
        else
        {
            String s=number.getText().toString();
            number.setText(s+b.getText().toString());
        }
    }
}


// ===============================================================================================
/*
    
    @Override
    public void onClick(View view) {
        Button b = (Button) view;
        String display = number.getText().toString();

        if (view == clear) {
            number.setText("");
            num1 = 0;
            num2 = 0;
            op = "";
        } else if (view == sub || view == add || view == mul || view == div) {
            // Parse the first number only
            if (!display.isEmpty()) {
                num1 = Double.parseDouble(display);
                op = b.getText().toString();
                // Keep first number visible and show operator
                number.setText(display + " " + op + " ");
            }
        } else if (view == equal) {
            if (!display.isEmpty() && display.contains(op)) {
                // Extract second number
                String[] parts = display.split(" ");
                if (parts.length < 3) return; // second number not entered yet
                num2 = Double.parseDouble(parts[2]);

                double result = 0;
                if (op.equals("+")) result = num1 + num2;
                else if (op.equals("-")) result = num1 - num2;
                else if (op.equals("*") || op.equals("×")) result = num1 * num2;
                else if (op.equals("/") || op.equals("÷")) {
                    if (num2 != 0) result = num1 / num2;
                    else {
                        number.setText(display + " = Error");
                        return;
                    }
                }

                // Show full operation and result
                number.setText(display + " = " + result);
            }
        } else {
            // Append typed number or decimal
            number.setText(display + b.getText().toString());
        }
    }
}

*/
