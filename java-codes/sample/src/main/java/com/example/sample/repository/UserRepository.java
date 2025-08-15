package com.example.sample.repository;

import java.util.List;
import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import com.example.sample.entity.User;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    
    // Otomatik sorgu metotları
    Optional<User> findByEmail(String email);
    
    List<User> findByNameContainingIgnoreCase(String name);
    
    // Custom query örneği
    @Query("SELECT u FROM User u WHERE u.name LIKE %?1%")
    List<User> findByNameContaining(String name);
    
    // Native query örneği
    @Query(value = "SELECT * FROM users WHERE email = ?1", nativeQuery = true)
    Optional<User> findUserByEmailNative(String email);
}
