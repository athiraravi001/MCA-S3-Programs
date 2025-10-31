package com.example.employeesalarycalculator;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity2 extends AppCompatActivity {

    TextView tResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        tResult = findViewById(R.id.tvResult);

        double basicPay = getIntent().getDoubleExtra("basicPay", 0.0);
        double hra = 0.2 * basicPay;
        double da = 0.3 * basicPay;
        double pf = 0.12 * basicPay;
        double netSalary = (basicPay + hra + da) - pf;

        String result = "Net Salary = ₹" + netSalary;
        tResult.setText(result);


        /* ---------- Using SharedPreferences ----------
        SharedPreferences sp = getSharedPreferences("EmployeeData", MODE_PRIVATE);
        String name = sp.getString("name", "");
        String designation = sp.getString("designation", "");
        double basicPayPref = Double.parseDouble(sp.getString("basicPay", "0"));

        double hraPref = 0.2 * basicPayPref;
        double daPref = 0.3 * basicPayPref;
        double pfPref = 0.12 * basicPayPref;
        double netSalaryPref = (basicPayPref + hraPref + daPref) - pfPref;

        String resultPref = "Name: " + name +
                "\nDesignation: " + designation +
                "\nBasic Pay: ₹" + basicPayPref +
                "\nHRA (20%): ₹" + hraPref +
                "\nDA (30%): ₹" + daPref +
                "\nPF (12%): ₹" + pfPref +
                "\n\nNet Salary: ₹" + netSalaryPref;

        tResult.setText(resultPref);
        */
    }

    public void onClick(View view) {
        Intent i2 = new Intent(MainActivity2.this, MainActivity.class);
        startActivity(i2);
        // finish();
    }
}