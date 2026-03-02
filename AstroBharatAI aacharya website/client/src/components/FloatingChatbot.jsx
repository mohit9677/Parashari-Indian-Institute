import React, { useState, useRef, useEffect } from 'react';
import ChatInterface from './ChatInterface';
import chatbotIdle from '../assets/chatbot_idle.webp';
import chatbotActive from '../assets/chatbot_active.webp';

const FloatingChatbot = () => {
    const [isOpen, setIsOpen] = useState(false);
    const [position, setPosition] = useState({ bottom: 32, right: 32 }); // 2rem = 32px
    const [isDragging, setIsDragging] = useState(false);
    const [isHovered, setIsHovered] = useState(false);
    const dragStartRef = useRef({ x: 0, y: 0 });
    const positionStartRef = useRef({ bottom: 32, right: 32 });

    const toggleChat = () => {
        if (!isDragging) setIsOpen(!isOpen);
    };

    const handleMouseDown = (e) => {
        if (isOpen) return; // Disable drag when chat is open
        setIsDragging(false);
        dragStartRef.current = { x: e.clientX, y: e.clientY };
        positionStartRef.current = { ...position };

        const handleMouseMove = (mm) => {
            const dx = dragStartRef.current.x - mm.clientX;
            const dy = dragStartRef.current.y - mm.clientY;

            if (Math.abs(dx) > 5 || Math.abs(dy) > 5) setIsDragging(true);

            let newRight = positionStartRef.current.right + dx;
            let newBottom = positionStartRef.current.bottom + dy;

            const padding = 10;
            const maxRight = window.innerWidth - 80;
            const maxBottom = window.innerHeight - 80;

            if (newRight < padding) newRight = padding;
            if (newRight > maxRight) newRight = maxRight;
            if (newBottom < padding) newBottom = padding;
            if (newBottom > maxBottom) newBottom = maxBottom;

            setPosition({
                right: newRight,
                bottom: newBottom
            });
        };

        const handleMouseUp = () => {
            document.removeEventListener('mousemove', handleMouseMove);
            document.removeEventListener('mouseup', handleMouseUp);
        };

        document.addEventListener('mousemove', handleMouseMove);
        document.addEventListener('mouseup', handleMouseUp);
    };

    const handleTouchStart = (e) => {
        if (isOpen) return;
        const touch = e.touches[0];
        setIsDragging(false);
        dragStartRef.current = { x: touch.clientX, y: touch.clientY };
        positionStartRef.current = { ...position };
    };

    const handleTouchMove = (e) => {
        const touch = e.touches[0];
        const dx = dragStartRef.current.x - touch.clientX;
        const dy = dragStartRef.current.y - touch.clientY;

        if (Math.abs(dx) > 5 || Math.abs(dy) > 5) setIsDragging(true);

        let newRight = positionStartRef.current.right + dx;
        let newBottom = positionStartRef.current.bottom + dy;

        const padding = 10;
        const maxRight = window.innerWidth - 80;
        const maxBottom = window.innerHeight - 80;

        if (newRight < padding) newRight = padding;
        if (newRight > maxRight) newRight = maxRight;
        if (newBottom < padding) newBottom = padding;
        if (newBottom > maxBottom) newBottom = maxBottom;

        setPosition({
            right: newRight,
            bottom: newBottom
        });
    };

    return (
        <div style={{
            position: 'fixed',
            bottom: `${position.bottom}px`,
            right: `${position.right}px`,
            zIndex: 1000,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'flex-end',
            gap: '1rem',
            touchAction: 'none'
        }}>
            {/* Chat Window Popover */}
            {isOpen && (
                <div style={{
                    width: '350px',
                    height: '500px',
                    background: '#fff',
                    borderRadius: '12px',
                    boxShadow: '0 4px 20px rgba(0,0,0,0.2)',
                    display: 'flex',
                    flexDirection: 'column',
                    overflow: 'hidden',
                    marginBottom: '10px',
                    animation: 'slideUp 0.3s ease-out'
                }}>
                    <ChatInterface isWidget={true} onClose={toggleChat} />
                </div>
            )}

            {/* Floating Icon Button */}
            <button
                onMouseDown={handleMouseDown}
                onTouchStart={handleTouchStart}
                onTouchMove={handleTouchMove}
                onClick={toggleChat}
                onMouseEnter={() => setIsHovered(true)}
                onMouseLeave={() => setIsHovered(false)}
                style={{
                    width: '90px',
                    // Let height be auto to accommodate text, but min-height keeps hit area
                    minHeight: '90px',
                    borderRadius: '0',
                    border: 'none',
                    background: 'transparent',
                    padding: 0,
                    cursor: isDragging ? 'grabbing' : 'pointer',
                    filter: isHovered
                        ? 'drop-shadow(0 8px 12px rgba(0,0,0,0.4))'
                        : 'drop-shadow(0 4px 6px rgba(0,0,0,0.3))',
                    overflow: 'visible',
                    transition: isDragging ? 'none' : 'transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), filter 0.3s ease',
                    transform: isOpen
                        ? 'scale(0.9)'
                        : isHovered
                            ? 'scale(1.1)'
                            : 'scale(1)',
                    display: 'flex',
                    flexDirection: 'column', // Stack vertical
                    justifyContent: 'center',
                    alignItems: 'center',
                    zIndex: 1001,
                    gap: '5px' // Space between image and text
                }}
            >
                <img
                    src={(isOpen || isHovered) ? chatbotActive : chatbotIdle}
                    alt="Chat with AI Baba"
                    style={{
                        width: '80px', // Slightly smaller image to fit comfortably
                        height: '80px',
                        objectFit: 'contain',
                        transition: 'opacity 0.2s ease-in-out'
                    }}
                    draggable={false}
                />
                <span style={{
                    display: 'inline-block',
                    background: 'rgba(255,255,255,0.9)', // Semi-transparent white
                    color: '#800000', // Maroon text for contrast
                    padding: '2px 8px',
                    borderRadius: '12px',
                    fontSize: '0.85rem',
                    fontWeight: 'bold',
                    boxShadow: '0 2px 5px rgba(0,0,0,0.2)',
                    whiteSpace: 'nowrap',
                    pointerEvents: 'none' // Let clicks pass to button
                }}>
                    AI Baba
                </span>
            </button>

            <style>
                {`
                    @keyframes slideUp {
                        from { opacity: 0; transform: translateY(20px); }
                        to { opacity: 1; transform: translateY(0); }
                    }
                `}
            </style>
        </div>
    );
};

export default FloatingChatbot;
