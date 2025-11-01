package com.example.studentresultevaluator;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity2 extends AppCompatActivity {
    TextView tName, tTotal, tPercentage;

    float percentage;
    Button bNext;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        tTotal = findViewById(R.id.tvTotal);
        tPercentage =findViewById(R.id.tvPercentage);
        bNext = findViewById(R.id.btnNext);

        String s1 = getIntent().getStringExtra("mark1");
        String s2 = getIntent().getStringExtra("mark2");
        String s3 = getIntent().getStringExtra("mark3");
        String s4 = getIntent().getStringExtra("mark4");

        int m1 = Integer.parseInt(s1);
        int m2 = Integer.parseInt(s2);
        int m3 = Integer.parseInt(s3);
        int m4 = Integer.parseInt(s4);

        int total = m1 + m2 + m3 + m4;
        percentage = total / 4.0f;

        tTotal.setText("Total Marks: " + total);
        tPercentage.setText("Percentage: " + percentage + "%");

    }

    public void onClick2(View view) {
        Intent i = new Intent(MainActivity2.this, MainActivity3.class);
        i.putExtra("percentage", percentage);
        startActivity(i);
    }
}