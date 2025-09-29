package com.example.sharedpreferences;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity2 extends AppCompatActivity {

    private TextView nameTextView, passTextView;
    private SharedPreferences sharedPreferences;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        // Initialize TextViews
        nameTextView = findViewById(R.id.tname);
        passTextView = findViewById(R.id.tpass);

        // Get SharedPreferences
        sharedPreferences = getSharedPreferences("Login", MODE_PRIVATE);

        // Retrieve stored username and password
        String username = sharedPreferences.getString("Username", "Not Found");
        String password = sharedPreferences.getString("Password", "Not Found");

        // Set values to TextViews
        nameTextView.setText(username);
        passTextView.setText(password);
    }
}