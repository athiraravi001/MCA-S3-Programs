/*
Develop an application to create 3 activities.
First activity for reading Name and four marks of a student,
Second activity for displaying the total mark and Percentage mark of the student,
Third activity for displaying the result student is pass or fail (Percentage Mark >= 50% Pass, Percentage Mark < 50% Fail)
*/

package com.example.studentresultevaluator;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    EditText name, mark1, mark2, mark3, mark4;
    Button btn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        name = findViewById(R.id.etName);
        mark1 = findViewById(R.id.etMark1);
        mark2 = findViewById(R.id.etMark2);
        mark3 = findViewById(R.id.etMark3);
        mark4 = findViewById(R.id.etMark4);
        btn = findViewById(R.id.btnNext);
    }

    public void onClick1(View view) {
        String sname = name.getText().toString();
        String s1 = mark1.getText().toString();
        String s2 = mark2.getText().toString();
        String s3 = mark3.getText().toString();
        String s4 = mark4.getText().toString();

        if (sname.isEmpty() || s1.isEmpty() || s2.isEmpty() || s3.isEmpty() || s4.isEmpty()) {
            Toast.makeText(this, "Please fill all fields...", Toast.LENGTH_SHORT).show();
            return;
        }

        int m1 = Integer.parseInt(s1);
        int m2 = Integer.parseInt(s1);
        int m3 = Integer.parseInt(s1);
        int m4 = Integer.parseInt(s1);

        Intent i = new Intent(MainActivity.this, MainActivity2.class);
        i.putExtra("name", sname);
        i.putExtra("mark1", s1);
        i.putExtra("mark2", s2);
        i.putExtra("mark3", s3);
        i.putExtra("mark4", s4);
        startActivity(i);
    }
}