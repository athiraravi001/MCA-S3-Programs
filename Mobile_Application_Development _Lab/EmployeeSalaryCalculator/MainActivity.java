/*
Develop an application to create 2 activities.
First activity for reading Name, Designation and Basic Pay of an employee,
Second activity for calculate the Net salary (Net Salary = (Basic Pay + HRA + DA) - PF)
(Hint: HRA = 20% of Basic pay, DA = 30% of Basic pay, PF = 12% of Basic Pay)
*/

package com.example.employeesalarycalculator;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    EditText empName, empDesignation, empBasicPay;
    Button btnCalc;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        empName = findViewById(R.id.etName);
        empDesignation = findViewById(R.id.etDesignation);
        empBasicPay = findViewById(R.id.etBasicPay);
        btnCalc = findViewById(R.id.etCalculate);
    }

    public void onClick(View view) {

        String name = empName.getText().toString();
        String designation = empDesignation.getText().toString();
        double basicPay = Double.parseDouble(empBasicPay.getText().toString());

        Intent i1 = new Intent(MainActivity.this, MainActivity2.class);
        i1.putExtra("name", name);
        i1.putExtra("designation", designation);
        i1.putExtra("basicPay", basicPay);
        startActivity(i1);
    }

    /* ---------- Using SharedPreferences ----------
    public void onClick(View view) {
        String name = empName.getText().toString();
        String designation = empDesignation.getText().toString();
        String basicPay = empBasicPay.getText().toString();

        SharedPreferences sp = getSharedPreferences("EmployeeData", MODE_PRIVATE);
        SharedPreferences.Editor ed = sp.edit();
        ed.putString("name", name);
        ed.putString("designation", designation);
        ed.putString("basicPay", basicPay);
        ed.apply();

        Intent i1 = new Intent(MainActivity.this, MainActivity2.class);
        startActivity(i1);
    }
    */
}
