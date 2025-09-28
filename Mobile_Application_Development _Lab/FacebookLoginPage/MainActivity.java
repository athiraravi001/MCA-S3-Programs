package com.example.facebookloginpage;

import android.os.Bundle;
import android.text.TextUtils;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    EditText usernameEditText, passwordEditText;
    Button loginButton;
    TextView forgotPasswordText, createAccountText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize views
        usernameEditText = findViewById(R.id.username);
        passwordEditText = findViewById(R.id.password);
        loginButton = findViewById(R.id.submit_button);
        forgotPasswordText = findViewById(R.id.forgot_password);
        createAccountText = findViewById(R.id.create_account_text);

        // Login button click
        loginButton.setOnClickListener(v -> {
            String username = usernameEditText.getText().toString().trim();
            String password = passwordEditText.getText().toString().trim();

            if (TextUtils.isEmpty(username)) {
                usernameEditText.setError("Enter username");
                return;
            }

            if (TextUtils.isEmpty(password)) {
                passwordEditText.setError("Enter password");
                return;
            }

            Toast.makeText(MainActivity.this, "Login Successful", Toast.LENGTH_SHORT).show();
        });

        // Forgot password click
        forgotPasswordText.setOnClickListener(v ->
                Toast.makeText(MainActivity.this, "Forgot Password clicked", Toast.LENGTH_SHORT).show()
        );

        // Create new account click
        createAccountText.setOnClickListener(v ->
                Toast.makeText(MainActivity.this, "Create New Account clicked", Toast.LENGTH_SHORT).show()
        );
    }
}
